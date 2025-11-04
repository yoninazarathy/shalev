import os
import sys
from openai import OpenAI
from dataclasses import dataclass, field
import difflib
import yaml
from pprint import pprint
from yaspin import yaspin


SIZE_LIMIT = 30000

try:
    client = OpenAI()
except:
    print(f"Problem with OpenAI client - check API key.", file=sys.stderr)
    sys.exit(1)

@dataclass
class ActionPrompt:
    agent_command_name: str
    main_source_label: str
    system_prompt: dict
    user_prompt: dict
    # additional_source_label: field(repr = False) QQQQ

def load_agent_configs_from_folder(folder_path: str) -> List[ActionPrompt]:
    agent_configs = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(os.path.join(folder_path, filename), 'r') as f:
                data = yaml.safe_load(f)
            action_prompt = ActionPrompt(**data)
            agent_configs[action_prompt.agent_command_name] = action_prompt
    return agent_configs


def agent_action(workspace_data: ShalevWorkspace, project_handle, action_handle, component_handle):
    # print(f"{workspace_data.action_prompts_folder=}")
    agent_configs = load_agent_configs_from_folder(workspace_data.action_prompts_folder) #QQQQ do someplace else
    try:
        action_prompt = agent_configs[action_handle]
    except KeyError:
        print(f"No agent action {action_handle}.", file=sys.stderr)
        sys.exit(1)
    component_path = os.path.join(workspace_data.projects[project_handle].components_folder, component_handle)
    try:
        file_size = os.path.getsize(component_path)
        if file_size > SIZE_LIMIT:
            raise ValueError(f"File {component_path} is too large ({file_size} bytes; limit is {SIZE_LIMIT} bytes).")
        with open(component_path, "r", encoding="utf-8") as f:
            component_text = f.read()
    except Exception as e:
        print(f"Failed to read component file: {e}", file=sys.stderr)
        sys.exit(1)    
    messages = make_LLM_messages(action_prompt, component_text)
    try:
        with yaspin(text="Waiting for LLM response...") as spinner:
            response = client.chat.completions.create(model="gpt-4o",messages=messages)
    except Exception as e:
        print(f"OpenAI API error: {e}")
        sys.exit(1)
    revised_component_text = response.choices[0].message.content
    # print(f"COMPONENT TEXT:\n{component_text}")
    # print(f"\nREVISED TEXT:\n{revised_component_text}")
    compare_strings_succinct(component_text, revised_component_text)

def make_LLM_messages(action_prompt, component_text):
    messages=[
                {
                "role": "system",
                "content": action_prompt.system_prompt["content"],
                },
                {
                "role": "user",
                "content": component_text
                }
            ]
    return messages

def compare_strings_succinct(original, corrected):
    diff = difflib.unified_diff(original.split(), corrected.split(), lineterm='')
    # Join and print the differences
    print('\n'.join(diff))


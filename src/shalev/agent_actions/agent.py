import os
import sys
from openai import OpenAI
from dataclasses import dataclass, field
# import difflib
import yaml
from pprint import pprint

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
            component_string = f.read()
    except Exception as e:
        print(f"Failed to read component file: {e}", file=sys.stderr)
        sys.exit(1)    
    messages = make_LLM_messages(action_prompt, component_string)
    try:
        response = client.chat.completions.create(model="gpt-4o",messages=messages)
    except Exception as e:
        print(f"OpenAI API error: {e}")
        sys.exit(1)
    response_string = response.choices[0].message.content
    print(response_string)

def make_LLM_messages(action_prompt, component_string):
    messages=[
                {
                "role": "system",
                "content": action_prompt.system_prompt["content"],
                },
                {
                "role": "user",
                "content": component_string
                }
            ]
    return messages

# def compare_strings_succinct(original, corrected):
#     diff = difflib.unified_diff(original.split(), corrected.split(), lineterm='')
#     # Join and print the differences
#     print('\n'.join(diff))

# def grammar_action(component, project_path='example_workspace'):
#     previous_dir = os.getcwd()
#     try:
#         os.chdir(os.path.join(project_path,'components'))

#         if not os.path.exists(component):
#             raise FileNotFoundError(f"Error: The file '{component}' was not found.")

#         with open(component, 'r') as file:
#             component_text = file.read()

#         response = client.chat.completions.create(
#             model="gpt-4o",
#             messages=[
#                 {
#                 "role": "system",
#                 "content": "You will be provided with text, and your task is to find grammatical errors in that text and make the minimal fix to them. Return the corrected text without any explanations. If there are no errors, return exactly the text you were given."
#                 },
#                 {
#                 "role": "user",
#                 "content": component_text
#                 }
#             ],
#         )
#         revised_component_text = response.choices[0].message.content

#         component_out_dir = os.path.join('..','components_out')
#         if not os.path.exists(component_out_dir):
#             os.makedirs(component_out_dir)
#             print(f"Created components_out directory: f{component_out_dir}")
#         component_out_path = os.path.join(component_out_dir, component+".output")
#         component_directory = os.path.dirname(component_out_path)
#         if component_directory:
#             os.makedirs(component_directory, exist_ok=True)
#         with open(component_out_path, 'w') as file:
#             file.write(revised_component_text)

#         # print(f"COMPONENT TEXT:\n{component_text}")
#         # print(f"\nREVISED TEXT:\n{revised_component_text}")
#         # compare_strings_succinct(component_text, revised_component_text)
#     finally:
#         os.chdir(previous_dir)

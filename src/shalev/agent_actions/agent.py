import os
from openai import OpenAI
from dataclasses import dataclass, field
# import difflib
import yaml
from pprint import pprint


client = OpenAI()

@dataclass
class ActionPrompt:
    agent_command_name: str
    main_source_label: str
    system_prompt: dict
    user_prompt: dict
    # additional_source_label: field(repr = False) QQQQ

def load_agent_configs_from_folder(folder_path: str) -> List[ActionPrompt]:
    agent_configs = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.yaml') or filename.endswith('.yml'):
            with open(os.path.join(folder_path, filename), 'r') as f:
                data = yaml.safe_load(f)
            agent_configs.append(ActionPrompt(**data))
    return agent_configs


def agent_action(workspace_data: ShalevWorkspace, project_handle, action_handle, component_handle):
    print(f"{workspace_data.action_prompts_folder=}")
    agent_configs = load_agent_configs_from_folder(workspace_data.action_prompts_folder) #QQQQ do someplace else
    # print(f"{workspace_data=}")
    # print(f"{project_handle=}")
    # print(f"{action_handle=}")
    # print(f"{component_handle=}")
    # action_prompt_template = action_prompt_templates[action]
    print(agent_configs)
#     make_LLM_messages(action_prompt_template)

# def make_LLM_messages(action_prompt_template):
#     pprint(action_prompt_template)

#     messages=[
#                 {
#                 "role": "system",
#                 "content": action_prompt_template["system_prompt"],
#                 },
#                 {
#                 "role": "user",
#                 "content": action_prompt_template["user_prompt"]
#                 }
#             ]
#     pprint(messages)


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

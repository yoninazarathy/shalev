import os
import sys
import yaml
# import glob
# from pathlib import Path

# def assign_short_names(components):
#     short_name_dict = {}
#     for component in components:
#         base_name = Path(component).stem
#         short_name = base_name[:4]
#         original_short_name = short_name
#         counter = 1
#         while short_name in short_name_dict:
#             short_name = f"{original_short_name[:3]}{counter}"  # Adjust length to ensure it's still 4 chars
#             counter += 1
#         short_name_dict[short_name] = component
#     return short_name_dict

def setup_workspace(fn = ".shalev.yaml"):
    try:
        with open(fn) as dot_shalev_file:
            dot_shalev_dict = yaml.safe_load(dot_shalev_file)
            if "workspace_folder" in dot_shalev_dict:
                workspace_folder = dot_shalev_dict["workspace_folder"]
            else:
                print(f"workspace_folder is not properly set in {fn}")
                sys.exit(1)
    except FileNotFoundError:
        print(f"Error: {fn} file does not exist", file=sys.stderr)
        sys.exit(1)
    # print("QQQQ:", workspace_folder) todo - log this is our workspace_folder
    try:
        fn = os.path.join(workspace_folder, "workspace_config.yaml")
        with open(fn) as config_file:
            workspace_data = yaml.safe_load(config_file)
            return workspace_data
    except FileNotFoundError:
        print(f"Error: {fn} file does not exist", file=sys.stderr)
        sys.exit(1)

    # workspace_name = config["workspace"]["name"]
    # # print(f"{workspace_name=}")
    # workspace_data["action_prompts_path"] = os.path.join(workspace_dir, config["workspace"]["action_prompts_folder"])

    # projects = config["workspace"]["projects"]
    # workspace_data["projects"] = {}
    # for project in projects:
    #     project_data = {}
    #     project_short_name = project["short_name"]
    #     project_data["name"] = project["name"]
    #     project_data["components_path"] = os.path.join(workspace_dir, project["project_folder"], project["components_folder"])
    #     project_data["supporting_files_path"] = os.path.join(workspace_dir, project["project_folder"], project["supporting_files_folder"])
    #     project_data["results_path"] = os.path.join(workspace_dir, project["project_folder"], project["results_folder"])
    #     project_data["build_path"] = os.path.join(workspace_dir, project["project_folder"], project["build_folder"])

    #     components_path = Path(project_data["components_path"])
    #     components = []
    #     for file_path in components_path.rglob("*"):
    #         if file_path.is_file():
    #             component_full_name = file_path.relative_to(components_path).as_posix()
    #             components.append(component_full_name)
    #     short_name_dict = assign_short_names(components)
    #     project_data["components_short"] = short_name_dict
        
    #     workspace_data["projects"][project_short_name] = project_data


    # return workspace_data

# def setup_action_prompt_templates(action_prompts_path):
#     action_prompt_templates = {}
#     for file_path in glob.glob(os.path.join(action_prompts_path, "*.yaml")):
#         with open(file_path, 'r') as file:
#             action_prompt_yaml_data = yaml.safe_load(file)
#             action_prompt_templates[action_prompt_yaml_data["agent_command_name"]] = action_prompt_yaml_data
#     return action_prompt_templates

# def workspace_info(workspace_data, action_prompt_templates):
#     print("Actions: ", ", ".join(action_prompt_templates.keys()))
#     print("Projects: ", ", ".join(workspace_data["projects"].keys()))
#     example_project = ""
#     example_component = ""
#     for project in workspace_data["projects"]:
#         short_component_names = list(workspace_data["projects"][project]["components_short"].keys())
#         if example_project == "":
#             example_project = project
#             example_component = short_component_names[0]
#         print(f"Components for {project}: ", end="")
#         print(", ".join(short_component_names) if len(short_component_names) > 0 else "NONE")

#     example_action = list(action_prompt_templates.keys())[0]
    
#     print(f"Example usage:\n\tshalev agent {example_action} {example_project} {example_component}")


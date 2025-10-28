import subprocess
import os
from pprint import pprint
from ..shalev_setup import *


def compose_action(shalev_project: ShalevProject):
    print("compose!!!!")
    # previous_dir = os.getcwd()
    # pprint(shalev_project)
    # print(get_project_by_handle(workspace_data, project_handle))
    # try:
    #     os.chdir(project["components_path"])
    #     complete_text = create_complete_text('root.tex')
    #     with open(os.path.join(project["build_path"],'composed_project.tex'), 'w') as file:
    #         file.write(complete_text)

    #     os.chdir(project["build_path"])
    #     print(os.getcwd())
    #     result = subprocess.run(['pdflatex', 
    #                             '-interaction=nonstopmode', 
    #                             f'-output-directory={project["build_path"]}',
    #                             os.path.join(project["build_path"],'composed_project.tex')], capture_output=True, text=True)

    #     if result.returncode == 0:
    #         print("LaTeX compilation successful!")
    #         print(f"Output document should be in {project["build_path"]}/composed_project.pdf")
    #     else:
    #         print("LaTeX compilation failed!")
    #         print("Error output:")
    #         print(result.stdout)
    # finally:
    #     os.chdir(previous_dir)
    
def process_file(file_path, processed_files=None):
    # Initialize the set to track already processed files (to avoid circular includes)
    if processed_files is None:
        processed_files = set()
    
    # Check if the file has already been processed to avoid recursion issues
    if file_path in processed_files:
        raise ValueError(f"Circular include detected with file: {file_path}")
    
    # Add the current file to the processed set
    processed_files.add(file_path)
    
    complete_text = []
    
    with open(file_path, 'r') as f:
        for line in f:
            # Check for the include statement
            if line.startswith('!!!>include(') and line.endswith(')\n'):
                # Extract the file to be included
                included_file = line[len('!!!>include('):-2].strip()
                
                # Generate the full path of the included file
                included_file_path = os.path.join(os.path.dirname(file_path), included_file)
                
                # Recursively process the included file
                included_text = process_file(included_file_path, processed_files)
                
                # Add the included text to the body
                complete_text.append(included_text)
            else:
                # Otherwise, just add the current line
                complete_text.append(line)
    
    return ''.join(complete_text)

# def create_complete_text(root_file):
#     try:
#         complete_text = process_file(root_file)
#         return complete_text
#     except Exception as e:
#         print(f"Error: {e}")
#         return None

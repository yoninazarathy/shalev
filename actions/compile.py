import subprocess
import os

def compile_action(project_path='example_project'):
    previous_dir = os.getcwd()
    try:
        os.chdir(os.path.join(project_path,'components'))
        complete_text = create_complete_text('root.tex')
        with open('../composed_project.tex', 'w') as file:
            file.write(complete_text)

    finally:
        os.chdir(previous_dir)

    result = subprocess.run(['pdflatex', 
                            '-interaction=nonstopmode', 
                            f'-output-directory={project_path}',
                            f'{project_path}/composed_project.tex'], capture_output=True, text=True)

    print(result.stdout)

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

def create_complete_text(root_file):
    try:
        complete_text = process_file(root_file)
        return complete_text
    except Exception as e:
        print(f"Error: {e}")
        return None

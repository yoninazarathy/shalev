import os
from openai import OpenAI
import difflib
import yaml

client = OpenAI()

def compare_strings_succinct(original, corrected):
    diff = difflib.unified_diff(original.split(), corrected.split(), lineterm='')
    # Join and print the differences
    print('\n'.join(diff))

def grammar_action(component, project_path='example_workspace'):
    previous_dir = os.getcwd()
    try:
        os.chdir(os.path.join(project_path,'components'))

        if not os.path.exists(component):
            raise FileNotFoundError(f"Error: The file '{component}' was not found.")

        with open(component, 'r') as file:
            component_text = file.read()

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                "role": "system",
                "content": "You will be provided with text, and your task is to find grammatical errors in that text and make the minimal fix to them. Return the corrected text without any explanations. If there are no errors, return exactly the text you were given."
                },
                {
                "role": "user",
                "content": component_text
                }
            ],
        )
        revised_component_text = response.choices[0].message.content

        component_out_dir = os.path.join('..','components_out')
        if not os.path.exists(component_out_dir):
            os.makedirs(component_out_dir)
            print(f"Created components_out directory: f{component_out_dir}")
        component_out_path = os.path.join(component_out_dir, component+".output")
        component_directory = os.path.dirname(component_out_path)
        if component_directory:
            os.makedirs(component_directory, exist_ok=True)
        with open(component_out_path, 'w') as file:
            file.write(revised_component_text)

        # print(f"COMPONENT TEXT:\n{component_text}")
        # print(f"\nREVISED TEXT:\n{revised_component_text}")
        # compare_strings_succinct(component_text, revised_component_text)
    finally:
        os.chdir(previous_dir)

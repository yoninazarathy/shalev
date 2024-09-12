import subprocess

def compile_action():

    compose()

    result = subprocess.run(['pdflatex', 
                            '-interaction=nonstopmode', 
                            '-output-directory=example_project',
                            'example_project/composed_project.tex'], capture_output=True, text=True)

    print(result.stdout)


def compose():
    #this will create composed_project.tex
    # result = subprocess.run(['ls'], cwd = 'example_project', capture_output=True, text=True)

    # # Print the command output
    # print(result.stdout)
    pass
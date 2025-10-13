import click
from pprint import pprint
from shalev.actions import *
# from shalev.shalev_setup import *

# workspace_data = setup_workspace()
# action_prompt_templates = setup_action_prompt_templates(workspace_data["action_prompts_path"])

@click.group()
def cli():
    pass

@click.command()
@click.argument('project')
def compile(project):
    compile_action(workspace_data, project)

@click.command()
@click.argument('action')
@click.argument('project')
@click.argument('component')
def agent(action, project, component):
    agent_action(workspace_data, action_prompt_templates, action, project, component)

@click.command()
@click.option('--long', is_flag=True, help="Show full info.")
def info(long):
    if long:
        pprint(workspace_data)
        pprint(action_prompt_templates)
    else:
        workspace_info(workspace_data, action_prompt_templates)


cli.add_command(agent)
cli.add_command(compile)
cli.add_command(info)

def main():
    cli()

if __name__ == '__main__':
    main()
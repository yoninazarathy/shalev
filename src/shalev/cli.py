import click
import structlog
from pprint import pprint

#################
# logging setup #
#################
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer()
    ]
)
log = structlog.get_logger()
# log.info("user_logged_in", user="alice", status="ok") #QQQQ consider if it is what we need


from shalev.agent_actions import *
from shalev.compose_actions import *
from shalev.shalev_setup import *

workspace_data = setup_workspace()
# action_prompt_templates = setup_action_prompt_templates(workspace_data["action_prompts_path"])

@click.group()
def cli():
    pass


##################
# shalev compose #
##################
@click.command()
@click.argument('project')
# @click.option('--project', default=".", help="Project name or path (default: current directory)")
def compose(project = "."):
    compose_action(get_project_by_handle(workspace_data, project))

################
# shalev agent #
################
@click.command()
@click.argument('action')
@click.argument('project')
@click.argument('component')
def agent(action, project, component):
    print(f"doing shalev action {action} on project {project} and component {component}")
    agent_action(workspace_data, project, action, component)
    # agent_action(workspace_data, action_prompt_templates, action, project, component)


#################
# shalev config #
#################
@click.command()
def config():
    print("doing config....QQQQ")

#################
# shalev status #
#################
@click.command()
# @click.option('--long', is_flag=True, help="Show full status.")
def status():
    pprint(workspace_data)
    # if long:
    #     pprint(workspace_data)
    #     pprint(action_prompt_templates)
    # else:
    #     workspace_status(workspace_data, action_prompt_templates)


###########################
# putting it all together #
###########################
cli.add_command(compose)
cli.add_command(agent)
cli.add_command(status)
cli.add_command(config)

def main():
    cli()

if __name__ == '__main__':
    main()
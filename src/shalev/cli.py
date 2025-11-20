import click
import structlog
import logging
from pprint import pprint

#################
# logging setup #
#################
logging.basicConfig(
    filename="commands_structlog.json",
    level=logging.INFO,
    format="%(message)s"
)

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso", key="time"),
        structlog.processors.JSONRenderer()
    ]
)
logger = structlog.get_logger()
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
def compose(project):
    compose_action(workspace_data.projects[project])

################
# shalev agent #
################
@click.command()
@click.argument('action')
@click.argument('projcomps', nargs=-1)
def agent(action, projcomps):
    for projcomp in projcomps:
        if projcomp.count('~') != 1:
            raise click.UsageError(f"'{projcomp}' is missing '~'. Format should be project~component")
    if len(projcomps) == 0:
        raise click.UsageError(f"Need at least one project~component pair")
    elif len(projcomps) == 1:
        project, component = projcomps[0].split('~', 1)
        agent_action_single_component(workspace_data, action, project, component)
    elif len(projcomps) == 2:
        source_project, source_component = projcomps[0].split('~', 1)
        dest_project, dest_component = projcomps[1].split('~', 1)
        agent_action_source_and_dest_components(workspace_data, action, source_project, source_component, dest_project, dest_component)

        # print(f"{source_project=}, {source_component=}, {dest_project=}, {dest_component=}")
    else:
        raise click.UsageError("Currently supporting only 1 or 2 project~component pairs")

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
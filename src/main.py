import click
import sys
import os

from actions import *

# actions_path = os.path.join(os.getcwd(), "actions")
# sys.path.append(actions_path)

# from compile import compile_action
# from grammar import grammar_action

hello()

@click.group()
def cli():
    pass

@click.command()
def agent():
    print("agent")

@click.command()
def composer():
    print("composer")

@click.command()
def status():
    print("status")

@click.command()
def config():
    print("config")

@click.command()
def compile():
    compile_action()

@click.command()
@click.argument('component')
def grammar(component):
    grammar_action(component)


cli.add_command(agent)
cli.add_command(composer)
cli.add_command(status)
cli.add_command(config)
cli.add_command(compile)
cli.add_command(grammar)

if __name__ == '__main__':
    cli()
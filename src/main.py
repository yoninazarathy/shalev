import click
import sys
import os

actions_path = os.path.join(os.getcwd(), "actions")
sys.path.append(actions_path)

from compile import *

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


cli.add_command(agent)
cli.add_command(composer)
cli.add_command(status)
cli.add_command(config)
cli.add_command(compile)

if __name__ == '__main__':
    cli()
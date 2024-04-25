import click

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

cli.add_command(agent)
cli.add_command(composer)
cli.add_command(status)
cli.add_command(config)

if __name__ == '__main__':
    cli()
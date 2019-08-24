''' CLI entry point for the knot '''
import click


@click.group()
def main():
    '''display help'''


@main.command()
def build():
    '''executes predefined docker build command'''

@main.command()
def run():
    '''executes predefined docker run command'''


@main.command()
def start():
    '''starts web ui'''

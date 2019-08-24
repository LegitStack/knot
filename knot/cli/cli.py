''' CLI entry point for the knot '''
import os
import click
import threading
from knot import config
from knot.lib import detect_server

@click.group()
def main():
    '''display help'''


@main.command()
def build():
    '''executes predefined docker build command'''
    os.chdir(config.project_path('..'))
    ext = 'bat' if os.name == 'nt' else 'sh'
    os.system(f'docker_build.{ext}')

@main.command()
def run():
    '''executes predefined docker run command'''
    os.chdir(config.project_path('..'))
    thread = threading.Thread(target=detect_server, args=([5001],))
    thread.start()
    ext = 'bat' if os.name == 'nt' else 'sh'
    os.system(f'docker_run.{ext}')



@main.command()
def start():
    '''starts web ui'''
    os.chdir(config.project_path('web'))
    os.system('python app.py')

import os
import yaml


def get(name: str = 'config') -> dict:
    ''' gets configuration out of the yaml file '''
    with open(project_path('config', f'{name}.yaml'), mode='r') as f:
        return yaml.load(f)


def put(name: str = 'config', data: dict = None) -> dict:
    data = data or {}
    with open(project_path('config', f'{name}.yaml'), mode='w') as f:
        yaml.dump(data, f, default_flow_style=False)


def env() -> str:
    return os.environ.get('knot_env')


def project_path(*args) -> str:
    ''' produces a path string of project path plus args '''
    if args:
        return os.path.abspath(os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            *args))
    return os.path.abspath(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

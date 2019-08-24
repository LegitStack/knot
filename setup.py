import os
from setuptools import setup, find_packages

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('readme.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

with open('version', 'r') as f:
    VERSION = f.read()

NAME = 'knot'

setup(
    name=NAME,
    version=VERSION,
    # namespace_packages=[NAME],
    description='a little wholeness',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=[f'{NAME}.{p}' for p in find_packages(where=NAME)],
    install_requires=[],
    python_requires='>=3.7.4',
    author='Jordan Miller',
    author_email='paradoxlabs@protonmail.com',
    url='https://github.com/LegitStack/knot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent', ],
    entry_points={
        'console_scripts': ['knot = knot.cli.cli:main', ]}, )

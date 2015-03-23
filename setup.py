try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'TODO',
    'author': 'Marc',
    'url': 'https://github.com/mbrc/hamster',
    'version': '0.0.1',
    'install_requires': ['nose', 'sqlalchemy'],
    'packages': ['hamster'],
    'scripts': [],
    'name': 'Hamster'
}

setup(**config)
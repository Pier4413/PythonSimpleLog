from setuptools import setup
from logger.metadata.__version__ import __version__

setup(
    name='logger',
    packages=['logger'],
    description='A simple wrapper for logging in Python',
    version=__version__,  # updated
    url='https://github.com/Pier4413/PythonSimpleLog',
    author='Panda',
    author_email='panda@delmasweb.net',
    keywords=['logger', 'logs', 'logging']
)

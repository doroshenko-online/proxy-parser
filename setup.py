from os.path import join, dirname
from setuptools import setup, find_packages

setup(
    name='proxy-parser',
    version='0.1',
    package_dir={'proxy': './proxy'},
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='dimad',
    include_package_data=True
)


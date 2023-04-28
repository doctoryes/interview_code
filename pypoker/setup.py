# -*- coding: utf-8 -*-

# Learn more: https://github.com/tidelift/pypoker/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pypoker',
    version='0.1.0',
    description='Sample scaffold for simple python app',
    long_description=readme,
    author='Matthew Ellis',
    author_email='mellis@tidelift.com',
    url='https://github.com/tidelift/pypoker',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

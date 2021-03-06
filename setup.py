#!/usr/bin/env python

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pybst',
    version='5000.0.0',
    url = 'https://github.com/dc-user/py-bst',
    download_url='https://github.com/dc-user/py-bst',
    description='Implements Binary Search Trees, AVL Trees, Splay Trees, and Red Black Trees in Python with plotting.',
    long_description=read('README.txt'),
    author='Tyler Sanderson',
    author_email='tylerbtbam@gmail.com',
    packages=['pybst'],
    requires=['networkx','matplotlib'],
    license='GNU GPL 3'
)

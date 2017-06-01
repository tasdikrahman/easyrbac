#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Tasdik Rahman
# @GPLv3 License
# @http://tasdikrahman.me
# @https://github.com/prodicus

from setuptools import setup, find_packages
from codecs import open
from os import path

from easyrbac import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='easyrbac',
    version=__version__,
    description='easyrbac: Role Based Access Control for humans',
    long_description=long_description,
    url='https://github.com/prodicus/easyrbac',
    download_url='https://github.com/prodicus/easyrbac/tarball/' + __version__,
    license='GPLv3',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: Implementation :: CPython',
      'Programming Language :: Python :: Implementation :: PyPy',
      "Topic :: Text Processing :: Linguistic",
    ],
    keywords='rbac',
    packages=find_packages(exclude=['docs', 'tests*', 'examples']),
    include_package_data=True,
    author='Tasdik Rahman',
    author_email='prodicus@outlook.com'
)
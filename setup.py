#!/usr/bin/env python

from setuptools import setup

setup(name='latex2anki',
      version='0.0.1',
      description='convert LaTeX flash cards to Anki',
      author='Juan M. Bello-Rivas',
      author_email='jmbr@superadditive.com',
      url='https://github.com/jmbr/latex2anki',
      install_requires=['texsoup'],
      scripts=['latex2anki'])

#!/usr/bin/env python

from setuptools import setup
import sys

script_name = 'urtimer'

with open(script_name) as f:
  meta = dict(
    (k.strip(' _'), eval(v)) for k, v in
      # There will be a '\n', with eval(), it's safe to ignore
      (line.split('=') for line in f if line.startswith('__'))
    )

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Environment :: Console',
  'Intended Audience :: End Users/Desktop',
  'License :: OSI Approved :: MIT License',
  'Natural Language :: English',
  'Operating System :: POSIX',
  'Programming Language :: Python :: 2',
  'Topic :: Utilities',
  ]

setup(
  name        = meta['program'],
  version     = meta['version'],
  license     = meta['license'],
  url         = meta['website'],

  description      = meta['description'],
  long_description = open('README.rst').read(),

  classifiers = classifiers,

  author       = meta['author'],
  author_email = meta['email'],
  
  scripts = [script_name],

  package_data = {
    '': ['*.rst'],
    },

  install_requires = ['distribute', 'urwid'],
  )

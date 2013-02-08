#!/usr/bin/env python

from setuptools import Command, setup
from distutils.command.build import build

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

class build_manpages(Command):

  description = 'build manpages'
  user_options = []

  def initialize_options(self):

    pass

  def finalize_options(self):

    pass

  def run(self):

    print('building manpages')
    with open('README.rst') as f:
      source = f.read()

    doc_parts = publish_parts(
      source,
      writer_name="manpage")

    with open('man/urtimer.1', 'w') as f:
      f.write(doc_parts['whole'])

setup_d = dict(
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

  data_files = [
    ('man/man1', ['man/urtimer.1']),
    ],

  install_requires = ['distribute', 'urwid'],
  )

try:
  from docutils.core import publish_parts
  build.sub_commands.append(('build_manpages', None))
  setup_d['cmdclass'] = {'build_manpages': build_manpages}
except ImportError:
  pass

if __name__ == '__main__':
  setup(**setup_d)

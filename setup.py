#!/usr/bin/env python
# Copyright (C) 2012-2013 by Yu-Jie Lin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from __future__ import print_function
import codecs
from distutils.command.build import build
from setuptools import Command, setup
import sys

# scripts to be exculded from checking
EXCLUDE_SCRIPTS = ()
script_name = 'urtimer'
CHECK_FILES = (script_name, '.')

# ============================================================================


class build_manpages(Command):

  description = 'build manpages'
  user_options = []

  def initialize_options(self):

    pass

  def finalize_options(self):

    pass

  def run(self):

    print('building manpages')
    with open('urtimer.1.rst') as f:
      source = f.read()

    doc_parts = publish_parts(
      source,
      writer_name="manpage")

    with codecs.open('man/urtimer.1', 'w', encoding='utf8') as f:
      f.write(doc_parts['whole'])


class cmd_pep8(Command):

  description = 'run pep8'
  user_options = []

  def initialize_options(self):

    pass

  def finalize_options(self):

    pass

  def run(self):

    try:
      import pep8
    except ImportError:
      print(('Cannot import pep8, you forgot to install?\n'
             'run `pip install pep8` to install.'), file=sys.stderr)
      sys.exit(1)

    p8 = pep8.StyleGuide()

    # do not include code not written in b.py
    p8.options.exclude += EXCLUDE_SCRIPTS
    # ignore four-space indentation error
    p8.options.ignore += ('E111', 'E121')

    print()
    print('Options')
    print('=======')
    print()
    print('Exclude:', p8.options.exclude)
    print('Ignore :', p8.options.ignore)

    print()
    print('Results')
    print('=======')
    print()
    report = p8.check_files(CHECK_FILES)

    print()
    print('Statistics')
    print('==========')
    print()
    report.print_statistics()
    print('%-7d Total errors and warnings' % report.get_count())


class cmd_pyflakes(Command):

  description = 'run Pyflakes'
  user_options = []

  def initialize_options(self):

    pass

  def finalize_options(self):

    pass

  def run(self):

    try:
      from pyflakes import api
      from pyflakes import reporter as modReporter
    except ImportError:
      print(('Cannot import pyflakes, you forgot to install?\n'
             'run `pip install pyflakes` to install.'), file=sys.stderr)
      sys.exit(1)

    from os.path import basename

    reporter = modReporter._makeDefaultReporter()

    # monkey patch for exclusion of pathes
    api_iterSourceCode = api.iterSourceCode

    def _iterSourceCode(paths):
      for path in api_iterSourceCode(paths):
        if basename(path) not in EXCLUDE_SCRIPTS:
          yield path
    api.iterSourceCode = _iterSourceCode

    print()
    print('Options')
    print('=======')
    print()
    print('Exclude:', EXCLUDE_SCRIPTS)

    print()
    print('Results')
    print('=======')
    print()
    warnings = api.checkRecursive(CHECK_FILES, reporter)
    print()
    print('Total warnings: %d' % warnings)

# ============================================================================

with open(script_name) as f:
  # There will be a '\n', with eval(), it's safe to ignore
  g = (line.split('=') for line in f if line.startswith('__'))
  meta = dict((k.strip(' _'), eval(v)) for k, v in g)

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Environment :: Console',
  'Intended Audience :: End Users/Desktop',
  'License :: OSI Approved :: MIT License',
  'Natural Language :: English',
  'Operating System :: POSIX',
  'Programming Language :: Python :: 2',
  'Programming Language :: Python :: 3',
  'Topic :: Utilities',
]

setup_d = dict(
  name=meta['program'],
  version=meta['version'],
  license=meta['license'],
  url=meta['website'],

  description=meta['description'],
  long_description=open('README.rst').read(),

  classifiers=classifiers,

  author=meta['author'],
  author_email=meta['email'],

  scripts=[script_name],

  package_data={
    '': ['*.rst'],
  },

  data_files=[
    ('man/man1', ['man/urtimer.1']),
  ],

  install_requires=['distribute', 'urwid'],
)

try:
  from docutils.core import publish_parts
  build.sub_commands.append(('build_manpages', None))
  setup_d['cmdclass'] = {
    'build_manpages': build_manpages,
    'pep8': cmd_pep8,
    'pyflakes': cmd_pyflakes,
  }
except ImportError:
  pass

if __name__ == '__main__':
  setup(**setup_d)

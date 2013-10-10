=======
urtimer
=======

---------------------------------------------------
A simple countdown timer and stopwatch using urwid.
---------------------------------------------------

:Author: Yu-Jie Lin <livibetter@gmail.com>
:Date: 2013-10-10
:Copyright: Copyright 2011-2013 Yu-Jie Lin. MIT License.
:Version: 0.6.0
:Manual section: 1
:Manual group: User Commands


Synopsis
========

**urtimer** [-h] [-v] [-d *DATE*] [-S] [-s] [-D] [-w *FILE*] [*TIME* [*TIME* ...]]

::

  +---------------------------------------------------------+
  |                                                         |
  |                                                         |
  |     ▄▀▀▀▄ ▄▀▀▀▄   ▄▀▀▀▄ █▀▀▀▀   ▄▀▀▀▄ ▄▀▀▀▄   ▄▀▀▀▄     |
  |     █   █ █   █ ▀ █   █ █     ▀ █   █ █   █   █   █     |
  |     █   █ █   █ ▄ █   █ ▀▀▀▀▄ ▄ █   █ █   █   █   █     |
  |     █   █ █   █   █   █     █   █   █ █   █   █   █     |
  |      ▀▀▀   ▀▀▀     ▀▀▀  ▀▀▀▀     ▀▀▀   ▀▀▀  ▀  ▀▀▀      |
  |                                                         |
  |                                                         |
  +---------------------------------------------------------+


Description
===========

TIME specify the countdown time in format of NUMBER[SUFFIX], SUFFIX can be 'd', 'h', 'm', 's'. Default is 's' if SUFFIX is omitted. TIME can be used multiple times and they will be summed up.

-h, --help     show this help message and exit
-v, --version  show program's version number and exit
-f FONT, --font FONT
               set font
-u, --utf8     force UTF-8 encoding
-d DATE, --date DATE
               calculate countdown from the date, for example, "5:35
               PM", "noon", or "tomorrow 1 am". This option ignores
               TIME, requires parsedatetime package
-S, --stopwatch
               stopwatch mode
-s, --start    start timer when urtimer starts
-D, --no-ds    do not show deciseconds
-T, --no-title
               do not set window title
-w FILE, --write-elapsed FILE
               write final elapsed time to FILE


Functions
=========

1. Countdown timer: when reaches zero, the program exits.
2. Stopwatch (``-S`` or ``--stopwatch``)


Controls
========

Keys
----

:Z/A: decrease/increase hour
:X/S: decrease/increase minute
:C/D: decrease/increase second
:Space: start/pause timer
:Q: quit the program

Mouse
-----

:Left-button: start/pause timer


Dependencies
============

urwid
  the UI library

parsedatetime
  only required for ``-d`` or ``--date`` option.

  .. code::

    pip install parsedatetime


Resources
=========

Website: https://bitbucket.org/livibetter/urtimer
PyPI: https://pypi.python.org/pypi/urtimer

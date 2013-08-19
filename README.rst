=======
urtimer
=======

-------------------------------------
A simple countdown timer using urwid.
-------------------------------------

:Author: Yu-Jie Lin <livibetter@gmail.com>
:Date: 2013-08-14
:Copyright: Copyright 2011-2013 Yu-Jie Lin. MIT License.
:Version: 0.3.0
:Manual section: 1
:Manual group: User Commands
 
Synopsis
========

**urtimer** [-h] [-v] [-d *DATE*] [-s] [-D] [*TIME* [*TIME* ...]]

Description
===========

TIME specify the countdown time in format of NUMBER[SUFFIX], SUFFIX can be 'd', 'h', 'm', 's'. Default is 's' if SUFFIX is omitted. TIME can be used multiple times and they will be summed up.

-h, --help     show this help message and exit
-v, --version  show program's version number and exit
-d, --date     calculate countdown from the date, for example, "5:35
               PM", "noon", or "tomorrow 1 am". This option ignores
               TIME, requires parsedatetime package
-s, --start    Start timer when urtimer starts
-D, --no-ds    do not show deciseconds

Functions
=========

1. Countdown timer: when reaches zero, the program exits.

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

Resources
=========

Website: https://bitbucket.org/livibetter/urtimer

=======
CHANGES
=======

.. contents:: **Releases**
  :local:


Development
===========

Release 0.6.1: 2014-07-20T10:02:49Z
===================================

* Makefile

  * rename target ``install_test`` to ``test_setup``
  * change invocation of virtualenv
  + test packages build
  + test with ``LC_ALL=C`` for locale specific issues

* fix certain locales causing ``UnicodeDecodeError`` in Python 3
* fix ``--version`` with Python 3 argparse


Release 0.6.0: 2013-10-10T08:26:48Z
===================================

+ add ``-f``, ``--font`` for changing default font. (#3)
+ add ``-u``, ``--utf8`` to force UTF-8 encoding. (#3)


Release 0.5.1: 2013-10-02T02:05:01Z
===================================

* minor changes to documentations


Release 0.5.0: 2013-09-29
=========================

+ add window title updating with ``-T``, ``--no-title`` option to turning off


Release 0.4.0: 2013-08-19
=========================

+ add stopwatch mode (``-S``, ``--stopwatch``) (#2)
+ add ``-w``, ``--write-elapsed`` to write final elapsed time to a file when exits (#2)
+ add ``-d``, ``--date`` using parsedatetime package to parse date string
+ add test target to Makefile


Release 0.3.0: 2013-08-14
=========================

+ add ``-D``, ``--no-ds`` option for turning off deciseconds (#1)


Release 0.2.1: 2013-08-11
=========================

+ add PEP8 and pyflakes checks


Release 0.2: 2013-02-08
=======================

+ add manpage
+ add time arguments and suffixes


Release 0.1.0: 2012-05-02
=========================

The first release.

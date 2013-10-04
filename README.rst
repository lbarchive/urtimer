=======
urtimer
=======

---------------------------------------------------
A simple countdown timer and stopwatch using urwid.
---------------------------------------------------

It looks like::

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

You can also watch a `demonstration clip`__.

__ http://youtu.be/ypqxhV5SIgE

.. contents:: **Contents**
  :local:


Features
========

* Modes

  - Countdown timer
  - Stopwatch (``-S`` or ``--stopwatch``)

* Support sleep-like suffixes like "d", "h", "m", and "s".
* Support countdown date (``-d`` or ``--date``) like "noon" or "tomorrow 1 am"
* Window title updating


Installation
============

You can install urtimer via pip:

.. code:: sh

  pip install urtimer


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

urwid_
  the UI library

parsedatetime_
  only required for ``-d`` or ``--date`` option.

  .. code:: sh

    pip install parsedatetime

.. _urwid: https://pypi.python.org/pypi/urwid/
.. _parsedatetime: https://pypi.python.org/pypi/parsedatetime/


Issues and Contributions
========================

Feel free to open an issue in `issue tracker`_ for bugs, feature requests, or pull requests.

.. _issue tracker: https://bitbucket.org/livibetter/urtimer/issues


Copyright
=========

urtimer is licensed under the MIT License, see COPYING_.

.. _COPYING: https://bitbucket.org/livibetter/urtimer/raw/tip/COPYING


Resources
=========

* PyPI_
* Website_

.. _PyPI: https://pypi.python.org/pypi/urtimer
.. _Website: https://bitbucket.org/livibetter/urtimer

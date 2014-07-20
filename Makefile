# Copyright (C) 2013, 2014 by Yu-Jie Lin
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

PACKAGE=urtimer
SCRIPT=urtimer

PY2_CMD=python2
PY3_CMD=python3
INSTALL_TEST_DIR=/tmp/$(PACKAGE)_install_test

BUILD_CMD=./setup.py sdist --formats gztar,zip

build:
	$(BUILD_CMD)

upload:
	$(BUILD_CMD) upload

test: test_pep8 test_pyflakes test_setup

test_%:
	@echo '========================================================================================='
	$(PY2_CMD) setup.py $(subst test_,,$@)
	@echo '-----------------------------------------------------------------------------------------'
	$(PY3_CMD) setup.py $(subst test_,,$@)

test_setup: test_setup_py2 test_setup_py3

test_setup_py2 test_setup_py3:
	@echo '========================================================================================='
	rm -rf $(INSTALL_TEST_DIR)
	$(eval PY_CMD = \
		$(if $(findstring py2,$@),\
			$(PY2_CMD),\
			$(if $(findstring py3,$@),\
				$(PY3_CMD),\
				$(error Do not know what to do with $@)\
			)\
		)\
	)
	$(PY_CMD) -m virtualenv $(INSTALL_TEST_DIR)
	LC_ALL=C $(PY_CMD) setup.py --version >/dev/null
	$(PY_CMD) $(BUILD_CMD)
	$(PY_CMD) setup.py sdist --dist-dir $(INSTALL_TEST_DIR)
	$(INSTALL_TEST_DIR)/bin/pip install $(INSTALL_TEST_DIR)/*.tar.gz
	@\
		CHK_VER="`$(PY_CMD) $(SCRIPT) --version 2>&1`";\
		cd $(INSTALL_TEST_DIR);\
		. bin/activate;\
		[ "`type $(SCRIPT)`" = "$(SCRIPT) is $(INSTALL_TEST_DIR)/bin/$(SCRIPT)" ] &&\
		[ "$$CHK_VER" = "`bin/$(SCRIPT) --version 2>&1`" ]
	rm -rf $(INSTALL_TEST_DIR)

.PHONY: build upload test_setup test_setup_py2 test_setup_py3

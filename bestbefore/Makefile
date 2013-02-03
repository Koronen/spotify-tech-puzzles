.PHONY: test unittest acceptancetest submit

PYTHON=python

default: test

test: unittest acceptancetest

unittest:
	$(PYTHON) bestbefore_test.py

acceptancetest:
	$(PYTHON) bestbefore.py < samples/sample1.in | diff samples/sample1.ans -
	$(PYTHON) bestbefore.py < samples/sample2.in | diff samples/sample2.ans -

submit:
	echo "" | mail -s bestbefore -a bestbefore.py puzzle@spotify.com


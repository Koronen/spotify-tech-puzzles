.PHONY: test unittest acceptancetest

PYTHON=python

default: test

test: unittest acceptancetest

unittest:
	$(PYTHON) catvsdog_test.py

acceptancetest:
	$(PYTHON) catvsdog.py < samples/sample1.in | diff samples/sample1.ans -


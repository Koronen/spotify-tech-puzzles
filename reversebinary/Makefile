.PHONY: test unittest acceptancetest

PYTHON=python

default: test

test: unittest acceptancetest

unittest:
	$(PYTHON) reversebinary_test.py

acceptancetest:
	$(PYTHON) reversebinary.py < samples/sample1.in | diff samples/sample1.ans -
	$(PYTHON) reversebinary.py < samples/sample2.in | diff samples/sample2.ans -


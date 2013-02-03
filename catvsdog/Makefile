.PHONY: test unittest acceptancetest submit

PYTHON=python

default: test

test: unittest acceptancetest

unittest:
	$(PYTHON) catvsdog_test.py

acceptancetest:
	$(PYTHON) catvsdog.py < samples/sample1.in | diff samples/sample1.ans -

submit:
	echo "" | mail -s catvsdog -a catvsdog.py puzzle@spotify.com


.PHONY: test unittest acceptancetest submit

PYTHON=python

default: test

test: unittest acceptancetest

unittest:
	$(PYTHON) zipfsong_test.py

acceptancetest:
	$(PYTHON) zipfsong.py < samples/sample1.in | diff samples/sample1.ans -
	$(PYTHON) zipfsong.py < samples/sample2.in | diff samples/sample2.ans -

submit:
	echo "" | mail -s zipfsong -a zipfsong.py puzzle@spotify.com


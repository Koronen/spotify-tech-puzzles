CC_FLAGS=-g -O3 -Wall

.PHONY: build test acceptancetest clean

default: test

build: lottery

lottery: lottery.c
	$(CC) $(CC_FLAGS) $^ -o $@

test: acceptancetest

acceptancetest: lottery
	./lottery < samples/sample1.in | diff samples/sample1.ans -
	./lottery < samples/sample2.in | diff samples/sample2.ans -
	./lottery < samples/sample3.in | diff samples/sample3.ans -
	./lottery < samples/sample4.in | diff samples/sample4.ans -

clean:
	rm lottery

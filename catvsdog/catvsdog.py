#!/usr/bin/env python

import sys

class CatVsDog:
    def __init__(self, c, d, v):
        self.numberOfCats = c
        self.numberOfDogs = d
        self.numberOfVoters = v

    def addVote(self, keep, throw):
        pass

    def maximumNumberOfSatisfiedVoters(self):
        maximumNumberOfSatisfiedVoters = 0

        return maximumNumberOfSatisfiedVoters

def main():
    n = int(sys.stdin.readline())

    for i in range(n):
        (c, d, v) = [int(j) for j in sys.stdin.readline().split(" ")]

        cvd = CatVsDog(c, d, v)
        for j in range(v):
            (keep, throw) = sys.stdin.readline().split(" ", 1)
            cvd.addVote(keep, throw)

        print cvd.maximumNumberOfSatisfiedVoters()

if __name__ == '__main__':
    main()


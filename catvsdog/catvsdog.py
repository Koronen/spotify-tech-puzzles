#!/usr/bin/env python

import sys

class CatVsDog:
    def __init__(self, c, d, v):
        self.numberOfCats = c
        self.numberOfDogs = d
        self.numberOfVoters = v
        self.angryVoters = {
            'keep': {
                'cats': [0 for i in range(c)],
                'dogs': [0 for i in range(d)],
            },
            'throw': {
                'cats': [0 for i in range(c)],
                'dogs': [0 for i in range(d)],
            },
        }

    def addVote(self, keep, throw):
        catsdogs = 'cats' if keep[0] == 'C' else 'dogs'
        self.angryVoters['throw'][catsdogs][int(keep[1:])-1] += 1

        catsdogs = 'cats' if throw[0] == 'C' else 'dogs'
        self.angryVoters['keep'][catsdogs][int(throw[1:])-1] += 1

    def maximumNumberOfSatisfiedVoters(self):
        maximumNumberOfSatisfiedVoters = 0

        for tc in range(self.numberOfCats):
            n = self.angryVoters['throw']['cats'][tc]
            for c in range(self.numberOfCats):
                if c != tc:
                    n += self.angryVoters['keep']['cats'][c]
            for d in range(self.numberOfDogs):
                n += self.angryVoters['keep']['dogs'][d]

            numberOfSatisfiedVoters = self.numberOfVoters - n/2

            if numberOfSatisfiedVoters > maximumNumberOfSatisfiedVoters:
                maximumNumberOfSatisfiedVoters = numberOfSatisfiedVoters

        for td in range(self.numberOfDogs):
            n = self.angryVoters['throw']['dogs'][td]
            for c in range(self.numberOfCats):
                n += self.angryVoters['keep']['cats'][c]
            for d in range(self.numberOfDogs):
                if d != td:
                    n += self.angryVoters['keep']['dogs'][d]

            numberOfSatisfiedVoters = self.numberOfVoters - n/2

            if numberOfSatisfiedVoters > maximumNumberOfSatisfiedVoters:
                maximumNumberOfSatisfiedVoters = numberOfSatisfiedVoters

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


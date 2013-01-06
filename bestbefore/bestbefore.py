#!/usr/bin/env

import sys
from itertools import permutations
from datetime import date

class BestBefore:
    def computeEarliestLegalDate(self, line):
        earliestLegalDate = None

        for permutation in permutations(self.splitInputLine(line)):
            candidate = self.tupleToDate(permutation)
            if candidate and (not earliestLegalDate or candidate < earliestLegalDate):
                earliestLegalDate = candidate

        if earliestLegalDate:
            return earliestLegalDate.isoformat()
        else:
            return "%s is illegal" % line.strip()

    def splitInputLine(self, line):
        return line.strip().split("/")

    def tupleToDate(self, line):
        try:
            return date(self.padYear(int(line[0])), int(line[1]), int(line[2]))
        except ValueError:
            return None

    def padYear(self, year):
        if year < 100:
            return 2000 + year
        else:
            return year

def main():
    for line in sys.stdin:
        print BestBefore().computeEarliestLegalDate(line)

if __name__ == '__main__':
    main()


#!/usr/bin/env

import sys

def reverseBinary(number):
    return int(bin(number)[2:][::-1], 2)

def main():
    for line in sys.stdin:
        print reverseBinary(int(line))

if __name__ == '__main__':
    main()


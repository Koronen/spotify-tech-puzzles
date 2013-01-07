#!/usr/bin/env python

import sys

class ZipfSong:
    def __init__(self):
        self.songs = []
        self.totalPlayCount = 0

    def addSong(self, i, f, s):
        self.songs.append((i, f, s))
        self.totalPlayCount += f

    def topQualitySongs(self, m):
        if m <= 0:
            return []

        return sorted(self.songs, cmp=self.compareSongs)[:m]

    def compareSongs(self, x, y):
        qd = cmp(self.songQuality(*y), self.songQuality(*x))
        if qd != 0:
            return qd
        else:
            return cmp(self.songIndex(*x), self.songIndex(*y))

    def songIndex(self, i, f, s):
        return i

    def songQuality(self, i, f, s):
        return 1.0 * 2**(i+1) * f / self.totalPlayCount

    def songTitle(self, i, f, s):
        return s


def main():
    (n, m) = [int(i) for i in sys.stdin.readline().split(" ")]

    zs = ZipfSong()
    for i in range(n):
        (fi, si) = sys.stdin.readline().split(" ", 1)
        zs.addSong(i, int(fi), si.strip())

    for s in map(lambda s: zs.songTitle(*s), zs.topQualitySongs(m)):
        print s

if __name__ == '__main__':
    main()


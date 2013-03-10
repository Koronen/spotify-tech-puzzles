#!/usr/bin/env python

import sys

class Song:
    def __init__(self, i, f, s):
        self.i = i
        self.f = f
        self.s = s

    def index(self):
        return self.i

    def playCount(self):
        return self.f

    def title(self):
        return self.s

    def __cmp__(self, other):
        return self.i - other.index()

class ZipfSong:
    def __init__(self):
        self.songs = []

    def addSong(self, song):
        self.songs.append(song)

    def topQualitySongs(self, m):
        if m <= 0:
            return []

        return sorted(self.songs, cmp=self.compareSongs, reverse=True)[:m]

    def compareSongs(self, x, y):
        qx = (1.0+x.index()) * x.playCount()
        qy = (1.0+y.index()) * y.playCount()
        qd = cmp(qx, qy)

        if qd != 0:
            return qd
        else:
            return -cmp(x.index(), y.index())

def main():
    (n, m) = [int(i) for i in sys.stdin.readline().split(" ")]

    zs = ZipfSong()
    for i in range(n):
        (fi, si) = sys.stdin.readline().split(" ", 1)
        zs.addSong(Song(i, int(fi), si.strip()))

    for s in map(lambda s: s.title(), zs.topQualitySongs(m)):
        print s

if __name__ == '__main__':
    main()


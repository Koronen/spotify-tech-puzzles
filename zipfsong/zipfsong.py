#!/usr/bin/env python

import sys

class ZipfSong:
    def __init__(self):
        self.songs = []
        self.firstSongPlayCount = -1

    def addSong(self, i, f, s):
        self.songs.append((i, f, s))

        if i == 0:
            self.firstSongPlayCount = f

    def topQualitySongs(self, m):
        if m <= 0:
            return []

        return sorted(self.songs, cmp=self.compareSongs, reverse=True)[:m]

    def compareSongs(self, x, y):
        expected_x_play_count = self.firstSongPlayCount / (1.0+self.songIndex(*x))
        expected_y_play_count = self.firstSongPlayCount / (1.0+self.songIndex(*y))
        qd = cmp(self.songPlayCount(*x) / expected_x_play_count, self.songPlayCount(*y) / expected_y_play_count)

        if qd != 0:
            return qd
        else:
            return -cmp(self.songIndex(*x), self.songIndex(*y))

    def songIndex(self, i, f, s):
        return i

    def songPlayCount(self, i, f, s):
        return f

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


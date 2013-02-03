#!/usr/bin/env python

import unittest

from zipfsong import ZipfSong

class TestZipfSong(unittest.TestCase):
    def test_topQualitySongs_no_songs_added(self):
        zs = ZipfSong()
        self.assertEquals(zs.topQualitySongs(3), [])

    def test_topQualitySongs_no_songs_requested(self):
        zs = ZipfSong()
        zs.addSong(0, 0, "")
        self.assertEquals(zs.topQualitySongs(0), [])

    def test_topQualitySongs_one_song(self):
        zs = ZipfSong()
        zs.addSong(0, 1, "Hi")
        self.assertEquals(zs.topQualitySongs(1), [(0, 1, "Hi")])

    def test_topQualitySongs_three_songs(self):
        zs = ZipfSong()
        zs.addSong(0, 10, "Foo")
        zs.addSong(1, 7, "Bar")
        zs.addSong(2, 5, "Baz")
        self.assertEquals(zs.topQualitySongs(3), [
            (2, 5, "Baz"),
            (1, 7, "Bar"),
            (0, 10, "Foo"),
        ])

if __name__ == '__main__':
    unittest.main()


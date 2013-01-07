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

if __name__ == '__main__':
    unittest.main()


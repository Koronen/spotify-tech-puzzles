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

    def test_topQualitySongs_first_song_no_plays(self):
        zs = ZipfSong()
        zs.addSong(0, 0, "Foo")
        zs.addSong(1, 10, "Bar")
        zs.addSong(2, 5, "Baz")
        self.assertEquals(zs.topQualitySongs(3), [
            (1, 10, "Bar"),
            (2, 5, "Baz"),
            (0, 0, "Foo"),
        ])

    def test_compareSongs_x_better(self):
        zs = ZipfSong()
        zs.addSong(0, 12, "x")
        self.assertEquals(zs.compareSongs(
            (0, 12, "x"),
            (1, 5, "y")
        ), 1)

    def test_compareSongs_y_better(self):
        zs = ZipfSong()
        zs.addSong(0, 10, "x")
        self.assertEquals(zs.compareSongs(
            (0, 10, "x"),
            (1, 7, "y")
        ), -1)

    def test_compareSongs_same_quality_x_first(self):
        zs = ZipfSong()
        zs.addSong(0, 10, "x")
        self.assertEquals(zs.compareSongs(
            (0, 10, "x"),
            (1, 5, "y")
        ), 1)

    def test_compareSongs_same_quality_y_first(self):
        zs = ZipfSong()
        zs.addSong(0, 10, "y")
        self.assertEquals(zs.compareSongs(
            (1, 5, "x"),
            (0, 10, "y")
        ), -1)

if __name__ == '__main__':
    unittest.main()


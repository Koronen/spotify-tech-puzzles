#!/usr/bin/env python

import unittest

from zipfsong import Song
from zipfsong import ZipfSong

class TestZipfSong(unittest.TestCase):
    def test_topQualitySongs_no_songs_added(self):
        zs = ZipfSong()
        self.assertEquals(zs.topQualitySongs(3), [])

    def test_topQualitySongs_no_songs_requested(self):
        zs = ZipfSong()
        zs.addSong(Song(0, 0, ""))
        self.assertEquals(zs.topQualitySongs(0), [])

    def test_topQualitySongs_one_song(self):
        zs = ZipfSong()
        zs.addSong(Song(0, 1, "Hi"))
        self.assertEquals(zs.topQualitySongs(1), [Song(0, 1, "Hi")])

    def test_topQualitySongs_three_songs(self):
        zs = ZipfSong()
        zs.addSong(Song(0, 10, "Foo"))
        zs.addSong(Song(1, 7, "Bar"))
        zs.addSong(Song(2, 5, "Baz"))
        self.assertEquals(zs.topQualitySongs(3), [
            Song(2, 5, "Baz"),
            Song(1, 7, "Bar"),
            Song(0, 10, "Foo"),
        ])

    def test_topQualitySongs_first_song_no_plays(self):
        zs = ZipfSong()
        zs.addSong(Song(0, 0, "Foo"))
        zs.addSong(Song(1, 10, "Bar"))
        zs.addSong(Song(2, 5, "Baz"))
        self.assertEquals(zs.topQualitySongs(3), [
            Song(1, 10, "Bar"),
            Song(2, 5, "Baz"),
            Song(0, 0, "Foo"),
        ])

    def test_compareSongs_x_better(self):
        zs = ZipfSong()
        zs.addSong(Song(0, 12, "x"))
        self.assertEquals(zs.compareSongs(
            Song(0, 12, "x"),
            Song(1, 5, "y")
        ), 1)

    def test_compareSongs_y_better(self):
        zs = ZipfSong()
        zs.addSong(Song(0, 10, "x"))
        self.assertEquals(zs.compareSongs(
            Song(0, 10, "x"),
            Song(1, 7, "y")
        ), -1)

    def test_compareSongs_same_quality_x_first(self):
        zs = ZipfSong()
        zs.addSong(Song(0, 10, "x"))
        self.assertEquals(zs.compareSongs(
            Song(0, 10, "x"),
            Song(1, 5, "y")
        ), 1)

    def test_compareSongs_same_quality_y_first(self):
        zs = ZipfSong()
        zs.addSong(Song(0, 10, "y"))
        self.assertEquals(zs.compareSongs(
            Song(1, 5, "x"),
            Song(0, 10, "y")
        ), -1)

if __name__ == '__main__':
    unittest.main()


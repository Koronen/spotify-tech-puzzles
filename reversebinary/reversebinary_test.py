#!/usr/bin/env python

import unittest
from reversebinary import reverseBinary

class TestReverseBinary(unittest.TestCase):

    def test_reverseBinary_one(self):
        self.assertEqual(reverseBinary(1), 1)

    def test_reverseBinary_two(self):
        self.assertEqual(reverseBinary(2), 1)

if __name__ == '__main__':
    unittest.main()


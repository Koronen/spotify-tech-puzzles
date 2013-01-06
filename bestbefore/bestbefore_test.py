#!/usr/bin/env python

import unittest
from bestbefore import BestBefore
from datetime import date

class TestBestBefore(unittest.TestCase):

    def setUp(self):
        self.bb = BestBefore()

    def test_splitInputLine_splits_line_correctly(self):
        self.assertEqual(self.bb.splitInputLine("02/4/67\n"), ['02', '4', '67'])

    def test_tupleToDate_converts_valid_date(self):
        self.assertEqual(self.bb.tupleToDate(("67", "02", "4")), date(2067, 2, 4))

    def test_padYear_pads_two_digit_years(self):
        self.assertEqual(self.bb.tupleToDate(("67", "02", "4")), date(2067, 2, 4))

    def test_padYear_does_not_pad_four_digit_years(self):
        self.assertEqual(self.bb.tupleToDate(("2067", "02", "4")), date(2067, 2, 4))

if __name__ == '__main__':
    unittest.main()


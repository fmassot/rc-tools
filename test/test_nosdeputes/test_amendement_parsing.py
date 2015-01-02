# -*- coding: utf-8 -*-

import datetime
import unittest

from nosdeputes.parsing.amendement_parsing import (
    parse_rectif, parse_amendement_sort, SortAmendement, parse_date, parse_num
)


class AmendementParsingTest(unittest.TestCase):
    def test_rectif_is_1(self):
        self.assertEquals(1, parse_rectif(u'76 (Rect)'))

    def test_recitf_is_0(self):
        self.assertEquals(0, parse_rectif(u'76'))

    def test_sort_is_removed(self):
        self.assertEquals(SortAmendement.removed.value, parse_amendement_sort(u'Retiré'))

    def test_parse_date(self):
        self.assertEquals(datetime.date(2014, 2, 12), parse_date('12/02/2014'))

    def parse_num_with_rectif(self):
        self.assertEquals(u'76', parse_num(u'76 (Rect)'))

    def parse_num_without_rectif(self):
        self.assertEquals(u'CL4', parse_num(u'CL4'))

if __name__ == '__main__':
    unittest.main()
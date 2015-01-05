# -*- coding: utf-8 -*-

import datetime
import unittest

from nosdeputes.parsing.amendement_parsing import (
    parse_rectif, parse_amendement_sort, SortAmendement, parse_date, parse_num, parse_amendement_url
)


class AmendementParsingTest(unittest.TestCase):
    def test_url_parsing_with_ABCD(self):
        parsed_data = parse_amendement_url('http://www.assemblee-nationale.fr/14/amendements/0235A/AN/242.asp')
        self.assertEquals('14', parsed_data.legislature)
        self.assertEquals('235', parsed_data.texteloi_id)
        self.assertEquals('242A', parsed_data.numero)

    def test_url_parsing_with_financianl_commissions(self):
        parsed_data = parse_amendement_url('http://www.assemblee-nationale.fr/14/amendements/1395A/CION_FIN/CF523.asp')
        self.assertEquals('14', parsed_data.legislature)
        self.assertEquals('1395', parsed_data.texteloi_id)
        self.assertEquals('CF523A', parsed_data.numero)

    def test_hash_with_letter_in_texteloi_id(self):
        parsed_data = parse_amendement_url('http://www.assemblee-nationale.fr/14/amendements/TA80/AN/6.asp')
        self.assertEquals('14', parsed_data.legislature)
        self.assertEquals('TA80', parsed_data.texteloi_id)
        self.assertEquals('6', parsed_data.numero)

    def test_url_parsing_with_commission(self):
        parsed_data = parse_amendement_url('http://www.assemblee-nationale.fr/14/amendements/2060/CSENTR/41.asp')
        self.assertEquals('14', parsed_data.legislature)
        self.assertEquals('2060', parsed_data.texteloi_id)
        self.assertEquals('CSENTR41', parsed_data.numero)

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
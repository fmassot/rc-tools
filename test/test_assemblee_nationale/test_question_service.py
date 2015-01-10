# -*- coding: utf-8 -*-

import unittest

from assemblee_nationale.service import QuestionSearchService


class QuestionParsingTest(unittest.TestCase):
    def test_get(self):
        service = QuestionSearchService()
        self.assertEquals(5, len(service.get(legislature=13, size=5)['results']))

    def test_iter(self):
        iterator = QuestionSearchService().iter(legislature=13, size=5)
        iterator.next()
        second_page_result = iterator.next()
        self.assertEquals(5, len(second_page_result['results']))

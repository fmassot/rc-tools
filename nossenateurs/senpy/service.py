# -*- coding: utf-8 -*-
from __future__ import division

import requests

from .parsing.question_search_result_parser import parse_question_search_result

__all__ = ['QuestionSearchService']


class QuestionSearchService(object):
    def __init__(self):
        self.search_url = "http://www.senat.fr/basile/rechercheQuestion.do?off=10&rch=qa&de=20150403&au=20160403&dp=1+an&radio=dp&appr=text&aff=ar&tri=dd&_na=QG"
        self.size = 10
        self.start_params = {
            'off': 0,
            'rch': 'qa',
            'de': '20150403',
            'au': '20160403',
            'dp': '1 an',
            'radio': 'dp',
            'appr': 'text',
            'aff': 'ar',
            'tri': 'dd',
            '_na': 'QG'
        }

    def get(self, params):
        return parse_question_search_result(requests.get(self.search_url, params=params).content)

    def iter(self):
        search_results = self.get(self.start_params)
        yield search_results

        for start in range(1, search_results.total_count, self.size):
            params = self.start_params.copy()
            next_params = params['off'] = (params['off'][0] + 10)
            yield self.get(next_params)
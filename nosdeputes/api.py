# -*- coding: utf-8 -*-

### API OF NOSDEPUTES.FR ###

import requests


class NDApi(object):
    def __init__(self):
        self.base_url = 'http://www.nosdeputes.fr'

    def synthese(self, month=None, format='json'):
        """
        month format: YYYYMM
        """
        if month is None:
            month = 'data'
        url = self.base_url + '/synthese/' + month + '/' + format

        if format == 'json':
            return requests.get(url).json()
        else:
            return requests.get(url).content

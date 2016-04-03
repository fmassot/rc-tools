# -*- coding: utf-8 -*-

### API OF NOSDEPUTES.FR ###

import requests
from fuzzywuzzy.process import extract


def memoize(f):
    cache = {}

    def aux(*args, **kargs):
        k = (args, tuple(sorted(kargs.items())))
        if k not in cache:
            cache[k] = f(*args, **kargs)
        return cache[k]
    return aux


class CPCApi(object):
    format = 'json'

    def __init__(self, type='depute', legislature=None):
        self.type = type
        self.type_plural = type + 's'

        if legislature:
            self.base_url = 'http://%s.www.nos%s.fr' % (legislature, self.type_plural)
        else:
            self.base_url = 'http://www.nos%s.fr' % self.type_plural

    def synthese(self, month=None):
        """
        month format: YYYYMM
        """
        if month is None:
            month = 'data'
        url = '%s/synthese/%s/%s' % (self.base_url, month, self.format)

        data = requests.get(url).json()
        return [depute[self.type] for depute in data[self.type_plural]]

    def parlementaire(self, slug_name):
        url = '%s/%s/%s' % (self.base_url, slug_name, self.format)
        return requests.get(url).json()[self.type]

    def search(self, q, page=1):
        url = '%s/recherche/%s?page=%s&format=%s' % (self.base_url, q, page, self.format)
        return requests.get(url).json()

    @memoize
    @property
    def parlementaires(self):
        url = '%s/%s/%s' % (self.base_url, self.type_plural, self.format)
        data = requests.get(url).json()
        return [depute[self.type] for depute in data[self.type_plural]]

    def search_parlementaires(self, q, limit=5):
        return extract(q, self.parlementaires, limit=limit)

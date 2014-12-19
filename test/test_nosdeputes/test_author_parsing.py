# -*- coding: utf-8 -*-

import unittest

from nosdeputes.parsing.author_parsing import parse_authors


class AuthorParsingTest(unittest.TestCase):
    def test_authors_1(self):
        authors = u"M. Dupr&#233;, Mme Bouziane"

        parsed_authors = parse_authors(authors)

        self.assertEquals(parsed_authors[0].sexe, u'H')
        self.assertEquals(parsed_authors[0].name, u'Dupré')
        self.assertEquals(parsed_authors[1].sexe, u'F')
        self.assertEquals(parsed_authors[1].name, u'Bouziane')


if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-

import re
import HTMLParser

from addict import Dict

HTML_PARSER = HTMLParser.HTMLParser()


def parse_authors(authors):
    """Return a list of dict with name, group and sexe"""

    authors = HTML_PARSER.unescape(authors)
    authors_list = re.split(',|et', authors)

    parsed_authors = []
    for author in authors_list:
        parsed_author = Dict()

        if 'M.' in author:
            parsed_author.sexe = 'H'
        else:
            parsed_author.sexe = 'F'

        parsed_author.name = re.split('(M.|Mme)( de)? ', author)[-1]

        parsed_authors.append(parsed_author)

    return parsed_authors
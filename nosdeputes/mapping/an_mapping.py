# -*- coding: utf-8 -*-

import hashlib

from nosdeputes.model import Amendement
from nosdeputes.parsing.amendement_parsing import parse_amendement_sort, parse_date, parse_num, parse_rectif
from nosdeputes.parsing.author_parsing import parse_authors


def an_to_nd_amendement_mapper(an_amendement):
    amendement = Amendement()

    amendement.source = an_amendement.url
    amendement.sous_amendement_de = parse_num(an_amendement.amend_parent)
    amendement.signataires = an_amendement.auteurs
    amendement.date = parse_date(an_amendement.date_badage)
    amendement.sujet = an_amendement.designation_article
    amendement.texte = an_amendement.dispositif
    amendement.expose = an_amendement.expose
    amendement.legislature = an_amendement.legislature
    amendement.numero = parse_num(an_amendement.num_amtxt)
    amendement.texteloi_id = an_amendement.num_init
    amendement.sort = parse_amendement_sort(an_amendement.sort)
    amendement.rectif = parse_rectif(an_amendement.num_amtxt)

    m = hashlib.md5()
    m.update(an_amendement.dispositif.encode('utf-8'))
    amendement.content_md5 = m.hexdigest()

    return amendement

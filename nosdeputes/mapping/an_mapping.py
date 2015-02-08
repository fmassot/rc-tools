# -*- coding: utf-8 -*-

import hashlib

from nosdeputes.model import Amendement
from nosdeputes.parsing.amendement_parsing import parse_amendement_sort, parse_date, parse_num, parse_rectif, parse_amendement_url


def an_to_nd_amendement_mapper(an_amendement):
    """
    :param an_amendement: anpy.model.Amendement
    :return: nosdeputes.model.Amendement
    """
    amendement = Amendement()

    parsed_url_data = parse_amendement_url(an_amendement.url)

    amendement.source = an_amendement.url
    amendement.sous_amendement_de = parse_num(an_amendement.amend_parent)
    amendement.signataires = an_amendement.auteurs
    amendement.date = parse_date(an_amendement.date_badage)
    amendement.sujet = an_amendement.designation_article
    amendement.texte = an_amendement.dispositif
    amendement.expose = an_amendement.expose
    amendement.legislature = parsed_url_data.legislature
    amendement.numero = parsed_url_data.numero
    amendement.texteloi_id = parsed_url_data.texteloi_id
    amendement.sort = parse_amendement_sort(an_amendement.sort)
    amendement.rectif = parse_rectif(an_amendement.num_amtxt)

    m = hashlib.md5()
    m.update(an_amendement.dispositif.encode('utf-8'))
    amendement.content_md5 = m.hexdigest()

    return amendement

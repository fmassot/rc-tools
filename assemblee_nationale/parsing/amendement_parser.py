# -*- coding: utf-8 -*-

import re

from assemblee_nationale.model import AmendementSummary, Amendement, AmendementSummaryResponse
from bs4 import BeautifulSoup, NavigableString


def parse_amendements_summary(url, json_response):
    """
    json schema :
    {
      infoGenerales: {
        nb_resultats, debut, nb_docs
      },
      data_table: 'id|numInit|titreDossierLegislatif|urlDossierLegislatif|instance|numAmend|urlAmend|designationArticle|designationAlinea|dateDepot|signataires|sort'
    }

    NB : the json response does not contain the dispositif and expose
    """

    amendements = []

    for row in json_response['data_table']:
        values = row.split('|')
        kwargs = dict((field, value) for field, value in zip(AmendementSummary._fields, values))
        kwargs['legislature'] = re.search('www.assemblee-nationale.fr/(\d+)/', kwargs['url']).groups()[0]
        amendements.append(AmendementSummary(**kwargs))

    return AmendementSummaryResponse(**{
        'url': url,
        'total_count': json_response['infoGenerales']['nb_resultats'],
        'start': json_response['infoGenerales']['debut'],
        'size': json_response['infoGenerales']['nb_docs'],
        'results': amendements
    })


def parse_amendement(url, html_response):
    soup = BeautifulSoup(html_response)

    meta_names = [
        'NUM_AMTXT', 'AMEND_PARENT', 'URL_DOSSIER', 'NUM_INIT', 'ETAPE', 'DELIBERATION', 'TITRE_INIT', 'NUM_PARTIE',
        'DESIGNATION_ARTICLE', 'URL_DIVISION', 'DESIGNATION_ALINEA', 'MISSION', 'AUTEURS', 'AUTEUR_ID', 'GROUPE_ID',
        'COSIGNATAIRES_ID', 'SEANCE', 'SORT', 'DATE_BADAGE', 'DATE_SORT', 'ORDRE_TEXTE', 'CODE', 'REFCODE',
        'LEGISLATURE',
    ]

    kwargs = dict((meta_name.lower(), soup.find('meta', attrs={'name': meta_name})['content'].strip()) for meta_name in meta_names)
    kwargs['dispositif'] = remove_inline_css(soup.find('dispositif').div).decode_contents().strip().replace('\n', '')
    kwargs['expose'] = remove_inline_css(soup.find('expose').div).decode_contents().strip().replace('\n', '')
    kwargs['url'] = url

    return Amendement(**kwargs)


def remove_inline_css(tag):
    for element in tag:
        if type(element) != NavigableString:
            del element["style"]
    return tag


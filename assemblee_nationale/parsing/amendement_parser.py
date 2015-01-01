# -*- coding: utf-8 -*-

import re

from addict import Dict
from bs4 import BeautifulSoup


def parse_amendements_json_response(json_response):
    # schema should be :
    # id|numInit|titreDossierLegislatif|urlDossierLegislatif|instance|numAmend|urlAmend|designationArticle|designationAlinea|
    # dateDepot|signataires|sort
    # NB : the json response does not contain the text and

    keys = json_response['infoGenerales']['description_schema'].split('|')

    amendements = []

    for row in json_response['data_table']:
        values = row.split('|')
        amendement = Dict((key, value) for key, value in zip(keys, values))
        amendement.legislature, amendement.texteloi_id = \
            re.search('www.assemblee-nationale.fr/(\d+)/amendements/(\d+)', amendement.urlAmend).groups()

        amendements.append(amendement)

    return Dict({
        'total_count': json_response['infoGenerales']['nb_resultats'],
        'page': json_response['infoGenerales']['debut'],
        'size': json_response['infoGenerales']['nb_docs'],
        'amendements': amendements
    })


def parse_amendement_html(url, html_response):
    soup = BeautifulSoup(html_response)
    amendement = Dict()

    mapper = {
        'NUM_AMTXT': 'numAmend',
        'AMEND_PARENT': 'amendParent',
        'URL_DOSSIER': 'urlDossier',
        'NUM_INIT': 'numInit',
        'ETAPE': 'etape',
        'DELIBERATION': 'deliberation',
        'TITRE_INIT': 'titreDossierLegislatif',
        'NUM_PARTIE': 'numPartie',
        'DESIGNATION_ARTICLE': 'designationArticle',
        'URL_DIVISION': 'urlDivision',
        'DESIGNATION_ALINEA': 'designationAlinea',
        'MISSION': 'mission',
        'AUTEURS': 'auteurs',
        'AUTEUR_ID': 'auteurId',
        'GROUPE_ID': 'groupeId',
        'COSIGNATAIRES_ID': 'cosignataireIds',
        'SEANCE': 'seance',
        'SORT': 'sort',
        'DATE_BADAGE': 'date_badage',
        'DATE_SORT' : 'date_sort',
        'ORDRE_TEXTE': 'ordre_texte',
        'CODE': 'code',
        'REFCODE': 'refcode',
        'LEGISLATURE': 'legislature',
    }

    for meta_name, field_key in mapper.items():
        amendement[field_key] = soup.find('meta', attrs={'name': meta_name})['content'].strip()

    amendement.dispositif = soup.find('dispositif').div.decode_contents().strip()
    amendement.expose = soup.find('expose').div.decode_contents().strip()
    amendement.url = url

    return amendement



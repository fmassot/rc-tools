# -*- coding: utf-8 -*-

from addict import Dict

def parse_amendement_json_response(json_response):
    # schema should be
    # id|numInit|titreDossierLegislatif|urlDossierLegislatif|instance|numAmend|urlAmend|designationArticle|designationAlinea|
    # dateDepot|signataires|sort

    keys = json_response['infoGenerales']['description_schema'].split('|')

    amendements = []

    for row in json_response['data_table']:
        values = row.split('|')
        amendements.append(Dict((key, value) for key, value in zip(keys, values)))

    return amendements

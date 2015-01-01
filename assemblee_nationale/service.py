# -*- coding: utf-8 -*-

import requests
from parsing.amendement_parser import parse_amendements_json_response, parse_amendement_html


class AmendementService(object):
    def __init__(self):

        self.base_url = "http://www2.assemblee-nationale.fr/recherche/query_amendements"
        self.default_params = {
            'typeDocument': 'amendement',
            'rows': 100,
            'format': 'html',
            'tri': 'ordreTexteasc',
            'typeRes': 'liste',
            'idArticle': None,
            'idAuteur': None,
            'numAmend': None,
            'idDossierLegislatif': None,
            'idExamen': None,
            'sort': None,
            'dateDebut': None,
            'dateFin': None,
            'periodeParlementaire': None,
            'texteRecherche': None
        }

    def get(self, **kwargs):
        params = self.default_params.copy()
        params.update(kwargs)
        return parse_amendements_json_response(requests.get(self.base_url, params=params).json())

    @staticmethod
    def get_amendement(url):
        return parse_amendement_html(requests.get(url).content)

    def get_amendement_order(self, id_dossier, id_examen):
        return [amendement.numAmend for amendement in self.get(idExamen=id_examen, idDossier=id_dossier)]

    def get_amendements(self, start_date, end_date=None, numero=None):
        """start_date / end_date : YYYY-MM-DD"""
        return self.get(dateDebut=start_date, dateFin=end_date, numAmend=None)
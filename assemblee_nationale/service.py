# -*- coding: utf-8 -*-
import requests
from parsing.amendement_parser import parse_amendement_json_response


class AmendementService(object):
    def __init__(self):

        self.base_url = "http://www2.assemblee-nationale.fr/recherche/query_amendements"
        self.default_params = {
            'typeDocument': 'amendement',
            'rows': 2500,
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
        return parse_amendement_json_response(requests.get(self.base_url, params=params).json())

    def get_amendement_order(self, id_dossier, id_examen):
        return [amendement.numAmend for amendement in self.get(idExamen=id_examen, idDossier=id_dossier)]

    def get_amendements(self, start_date, end_date=None):
        """start_date / end_date : YYYY-MM-DD"""
        return self.get(dateDebut=start_date, dateFin=end_date)
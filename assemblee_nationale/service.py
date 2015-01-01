# -*- coding: utf-8 -*-
from __future__ import division

import requests
from parsing.amendement_parser import parse_amendements_json_response, parse_amendement_html


class AmendementService(object):
    def __init__(self):
        self.base_url = "http://www2.assemblee-nationale.fr/recherche/query_amendements"
        self.default_params = {
            'typeDocument': 'amendement',
            'rows': 100,
            'format': 'html',
            'tri': 'ordreTextedesc',
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
            'texteRecherche': None,
            'start': None,
        }

    def _get_amendements_summary(self, **kwargs):
        params = self.default_params.copy()
        params.update(kwargs)
        response = requests.get(self.base_url, params=params)
        return parse_amendements_json_response(response.json())

    def get_amendements_summary(self, start_date, end_date=None, numero=None, size=100, start=None):
        # FIXME : do we really want to rewrite parameters' names ?
        return self._get_amendements_summary(dateDebut=start_date, dateFin=end_date, numAmend=numero, rows=size, start=start)

    def get_total_count(self, start_date, end_date=None, numero=None):
        # First get total number of pages
        response = self.get_amendements_summary(start_date, end_date=end_date, numero=numero, size=1)
        return response.total_count

    def iter_on_amendements_summary(self, start_date, end_date=None, numero=None, size=100):
        # First get total number of pages
        response = self.get_amendements_summary(start_date, end_date=end_date, numero=numero, size=1)

        for start in range(0, response.total_count, size):
            yield self.get_amendements_summary(start_date, end_date=end_date, numero=numero, size=size, start=start)

    def get_amendement_order(self, id_dossier, id_examen):
        return [amendement.numAmend for amendement in self._get_amendements_summary(idExamen=id_examen, idDossier=id_dossier).amendements]

    @staticmethod
    def get_amendement(url):
        return parse_amendement_html(url, requests.get(url).content)
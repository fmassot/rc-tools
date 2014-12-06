# -*- coding: utf-8 -*-
import re
import requests


class AmendementService(object):
    def __init__(self):
        self.base_url = "http://www2.assemblee-nationale.fr/recherche/query_amendements"
        self.default_params = {
            'typeDocument': 'amendement',
            'rows: 2500,'
            'format': 'html',
            'tri': 'ordreTexteasc',
            'typeRes': 'liste'
        }

    def get(self, **kwargs):
        params = self.default_params.copy()
        params.update(kwargs)
        return requests.get(self.base_url, params=params).json()["data_table"]

    def get_amendement_order(self, id_dossier, id_examen):
        re_clean_num = re.compile(r"\D")

        amendements = []
        for line in self.get(idExamen=id_examen, idDossier=id_dossier):
            amendements.append(re_clean_num.sub("", line.split("|")[5]))

        return amendements

    def get_amendements(self):
        pass


class QuestionService(object):
    def get(self, url):
        return requests.get(url).data

    def parse(self, url):
        data = self.get(url)

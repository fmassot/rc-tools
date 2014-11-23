# -*- coding: utf-8 -*-
from commons.repository import Repository
from interets_parlementaires.db import mysql_db

ParlementarianDataType = {
    1: u'donnees_personnelles',
    2: u'activites_professionnelles',
    3: u'activites_pro_5ans',
    4: u'activites_conseil',
    5: u'organes_dirigeants',
    6: u'participations_financieres',
    7: u'activites_conjoint',
    8: u'fonctions_benevoles',
    9: u'fonctions_mandats',
    10: u'collaborateurs',
    11: u'activites_conservees',
    12: u'observations',
    13: u'dates_reception',
}


class ParlementarianRepository(Repository):
    def __init__(self, db=mysql_db):
        super(ParlementarianRepository, self).__init__(db)

    def get_parlementarians(self, ptype='all'):
        if ptype == 'all':
            like = '%'
        elif ptype == 'depute':
            like = 'http://www.nosdeputes.fr%'
        elif ptype == 'senateur':
            like = 'http://www.nossenateurs.fr%'

        sql = "SELECT DISTINCT parlementaire FROM documents WHERE parlementaire_avatarurl LIKE %s"
        self.cursor.execute(sql, (like,))
        return zip(*self.cursor.fetchall())[0]

    def get_senateurs(self):
        sql = "SELECT DISTINCT parlementaire FROM documents WHERE url LIKE "
        self.cursor.execute(sql)
        return zip(*self.cursor.fetchall())[0]

    def get_data_by_type(self, type):
        sql = """SELECT parlementaire, data FROM tasks, documents
              WHERE documents.selected_task = tasks.id AND done = 1 AND type = %s
              """
        self.cursor.execute(sql, (type,))
        return self.cursor.fetchall()



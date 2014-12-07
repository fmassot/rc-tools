# -*- coding: utf-8 -*-
from commons.repository import Repository
from commons.mysql_cursor import MappedCursor
from nosdeputes.model import Amendement, Parlementaire
from nosdeputes.db import mysql_db


class AmendementCursor(MappedCursor):
    map_function = Amendement


class AmendementRepository(Repository):
    def __init__(self, db=mysql_db):
        super(AmendementRepository, self).__init__(db, cursorclass=AmendementCursor)

    def get_by_numero(self, numero):
        self.cursor.execute("SELECT * FROM amendement WHERE numero = %s", (numero,))
        return self.cursor.fetchone()

    def get_by_texteloi_id(self, texteloi_id):
        self.cursor.execute("SELECT * FROM amendement WHERE texteloi_id = %s", (texteloi_id,))
        return self.cursor.fetchall()


class ParlementaireCursor(MappedCursor):
    map_function = Parlementaire


class ParlementaireRepository(Repository):
    def __init__(self, db=mysql_db):
        super(ParlementaireRepository, self).__init__(db, cursorclass=ParlementaireCursor)

    def get_by_numero(self, numero):
        self.cursor.execute("SELECT * FROM amendement WHERE numero = %s", (numero,))
        return self.cursor.fetchone()

    def get_by_texteloi_id(self, texteloi_id):
        self.cursor.execute("SELECT * FROM amendement WHERE texteloi_id = %s", (texteloi_id,))
        return self.cursor.fetchall()
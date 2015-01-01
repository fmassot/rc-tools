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

    def get_by_url(self, url):
        self.cursor.execute("SELECT * FROM amendement WHERE source = %s", (url,))
        return self.cursor.fetchone()

    def find_by_url(self, urls):
        self.cursor.execute("SELECT * FROM amendement WHERE source IN %s", (urls,))
        return self.cursor.fetchall()

    def get(self, numero, legislature, loi, rectif):
        self.cursor.execute(
            """SELECT * FROM amendement
            WHERE numero = %s AND legislature = %s AND loi = %s AND rectif = %s
            """,
            (numero, legislature, loi, rectif)
        )

        return self.cursor.fetchone()

    def find_by_texteloi_id(self, texteloi_id):
        self.cursor.execute("SELECT * FROM amendement WHERE texteloi_id = %s", (texteloi_id,))
        return self.cursor.fetchall()


class ParlementaireCursor(MappedCursor):
    map_function = Parlementaire


class ParlementaireRepository(Repository):
    def __init__(self, db=mysql_db):
        super(ParlementaireRepository, self).__init__(db, cursorclass=ParlementaireCursor)


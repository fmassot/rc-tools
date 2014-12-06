# -*- coding: utf-8 -*-
from commons.repository import Repository
from nosdeputes.db import mysql_db

"""
| id                 |
| nb_commentaires    |
| source             |
| legislature        |
| texteloi_id        |
| numero             |
| sous_amendement_de |
| rectif             |
| sujet              |
| sort               |
| date               |
| signataires        |
| texte              |
| expose             |
| content_md5        |
| nb_multiples       |
| created_at         |
| updated_at         |
"""


class AmendementRepository(Repository):
    def __init__(self, db=mysql_db):
        super(AmendementRepository, self).__init__(db)

    def get_by_numero(self, numero):
        self.cursor.execute("SELECT * FROM amendement WHERE numero = %s", (numero,))
        return self.cursor.fetchone()

    def get_by_texteloi_id(self, texteloi_id):
        self.cursor.execute("SELECT * FROM amendement WHERE texteloi_id = %s", (texteloi_id,))
        return self.cursor.fetchall()


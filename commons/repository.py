# -*- coding: utf-8 -*-

from pymysql import connect
from pymysql.cursors import DictCursor


class Repository(object):
    def __init__(self, db=None, cursorclass=DictCursor):
        self.db = db
        self.cursorclass = cursorclass
        self._cursor = None
        self._conn = None


    @property
    def conn(self):
        if self._conn is None:
            self._conn = connect(**self.db)

        return self._conn

    @property
    def cursor(self):
        if self._cursor is None:
            self._cursor = self.conn.cursor(cursor=self.cursorclass)

        return self._cursor

    def close(self):
        if self._cursor is not None:
            self._cursor.close()
            self._cursor = None

        if self._conn is not None:
            self._conn.close()
            self._conn = None
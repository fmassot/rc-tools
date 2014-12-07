# -*- coding: utf-8 -*-

from pymysql.cursors import Cursor


class MappedCursor(Cursor):
    map_function = None

    def _do_get_result(self):
        super(MappedCursor, self)._do_get_result()
        fields = []
        if self.description:
            for f in self._result.fields:
                name = f.name
                if name in fields:
                    name = f.table_name + '.' + name
                fields.append(name)
            self._fields = fields

        if fields and self._rows:
            self._rows = [self._conv_row(r) for r in self._rows]

    def _conv_row(self, row):
        if row is None:
            return None
        return self.map_function(**dict(zip(self._fields, row)))
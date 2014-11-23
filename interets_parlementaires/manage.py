# -*- coding: utf-8 -*-

import click

from json import loads
from commons.utf8_csv import UnicodeWriter
from .repository import ParliamentarianRepository

NO_DATA_STRING = u'NÉANT'

@click.group()
def cli():
    pass

@cli.command()
@cli.argument('type')
@cli.argument('output')
def export(type, output):
    repository = ParliamentarianRepository()
    parlementarians = repository.get_all_parlementarians()
    all_data = repository.get_data_by_type(type)

    data_by_parlementarian = dict((parlementarian, loads(json_data) for parlementarian, json_data in all_data))

    rows = []
    for parlementarian in parlementarians:
        if parlementarian in data_by_parlementarian:
            row = [parlementarian]
            for element in data_by_parlementarian[parlementarian]:
                rows.append(row + [element])
        else:
            row = [parlementarian, NO_DATA_STRING]
            rows.append(row)

    rows.sort()

    writer = UnicodeWriter(output)
    writer.writerows(rows)

if __name__ == '__main__':
    cli()



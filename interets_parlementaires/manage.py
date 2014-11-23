# -*- coding: utf-8 -*-

import click
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parents[1]))
from json import loads
from commons.utf8_csv import UnicodeWriter
from interets_parlementaires.repository import ParlementarianRepository, ParlementarianDataType

NO_DATA_STRING = u'NÉANT'

@click.group()
def cli():
    pass

@cli.command()
@click.option('--parlementarian_type', default='all', help='all|senateur|depute')
@click.option('--output-dir', default=None)
def export(parlementarian_type, output_dir):
    if not output_dir:
        output_dir = os.getcwd()

    repository = ParlementarianRepository()
    parlementarians = repository.get_parlementarians(ptype=parlementarian_type)

    for data_type, data_type_name in ParlementarianDataType.items():
        all_data = repository.get_data_by_type(data_type)

        data_by_parlementarian = dict([(parlementarian, loads(json_data)) for parlementarian, json_data in all_data])

        rows = []
        for parlementarian in parlementarians:
            if parlementarian in data_by_parlementarian:
                for element in data_by_parlementarian[parlementarian]:
                    row = [parlementarian]
                    for subelement in element:
                        row.append(subelement.replace(u'/néant/i', NO_DATA_STRING))
                    rows.append(row)
            else:
                row = [parlementarian, NO_DATA_STRING]
                rows.append(row)

            rows.sort()

            with open(os.path.join(output_dir, '%s_%s.csv' % (data_type_name, data_type)), 'w') as f:
                writer = UnicodeWriter(f, delimiter=';')
                writer.writerows(rows)


if __name__ == '__main__':
    cli()

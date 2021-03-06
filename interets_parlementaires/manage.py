# -*- coding: utf-8 -*-

import re
import os
import sys

import click
from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parents[1]))
from json import loads
from commons.utf8_csv import UnicodeWriter
from interets_parlementaires.repository import ParlementaireRepository, ParlementarianDataType

NO_DATA_STRING = u'NÉANT'

@click.group()
def cli():
    pass

@cli.command()
@click.option('--parlementaire-type', default='all', help='all|senateur|depute')
@click.option('--output-dir', default=None)
def export(parlementaire_type, output_dir):
    if not output_dir:
        output_dir = os.getcwd()

    repository = ParlementaireRepository()
    parlementaires = repository.get_parlementaires(ptype=parlementaire_type)

    headers_by_data_type = {
        1: u'parlementaire;année de naissance;profession',
        2: u'parlementaire;description de l\'activité professionnelle à la date de l\'élection;rémunération ou gratification perçue',
        3: u'parlementaire;description de l\'activité professionnelle exercée au cours des 5 dernières années;rémunération ou gratification perçue',
        4: u'parlementaire;identification de l\'employeur ou la structure sociale d\'emploi;description de l\'activité professionnelle de consultant exercée à la date de l\'élection ou au cours des 5 dernières années;rémunération ou gratification perçue',
        5: u'parlementaire;identification de l\'organisme public ou privé ou de la société;description de l\'activité (participation aux organses dirigeants) à la date de l\'élection ou au cours des 5 dernières années;rémunération ou gratification perçue',
        6: u'parlementaire;identification de la société;évaluation de la participation financière directe dans le capital;rémunération ou gratification perçue',
        7: u'parlementaire;description de l\'activité professionnelle du conjoint, partenaire lié par un PACS ou concubin',
        8: u'parlementaire;identification de la structure ou personne morale;description des activités et responsabilités exercées (fonctions bénévoles)',
        9: u'parlementaire;identification des fonctions et mandats électifs;date de début et de fin de fonction et mandat;rémunérations, indemnités ou gratifications perçuese',
        10: u'parlementaire;noms des collaborateurs parlementaires;identification de l\'employeur ou de la structure sociale d\'emploi;description d\'exercice de l\'activité professionelle',
        11: u'parlementaire;identification de l\'employeur ou de la structure sociale d\'emploi;description et modalité d\'exercice de l\'activité professionnelle ou d\'intérêt général conservée par le parlementaire;rémunérations, indemnités ou gratifications perçues',
        12: u'parlementaire;observations',
        13: u'parlementaire;date de dépôt',
    }

    for data_type, data_type_name in ParlementarianDataType.items():
        all_data = repository.get_data_by_type(data_type)

        data_by_parlementaire = dict([(row['parlementaire'], loads(row['data'])) for row in all_data])

        rows = []
        for parlementaire in parlementaires:
            if parlementaire in data_by_parlementaire:
                parlementaire_data = data_by_parlementaire[parlementaire]

                if type(parlementaire_data) == unicode:
                    parlementaire_data = [[NO_DATA_STRING]]

                for element in parlementaire_data:
                    row = [parlementaire]
                    for sub_element in element:
                        row.append(re.sub(r'[\n\r]+', ' ', re.sub(u'n[é,e]ant(?i)', NO_DATA_STRING, sub_element)))
                    rows.append(row)

            else:
                row = [parlementaire, NO_DATA_STRING]
                rows.append(row)

            rows.sort()

            with open(os.path.join(output_dir, '%02d_%s.csv' % (data_type, data_type_name)), 'w') as f:
                # choose '|' as quote to avoid double single or double quotes
                writer = UnicodeWriter(f, delimiter=';', quotechar='|', lineterminator='\n')
                writer.writerow(headers_by_data_type[data_type].split(';'))
                writer.writerows(rows)


if __name__ == '__main__':
    cli()

# -*- coding: utf-8 -*-

import click
import requests
import sys
import json
from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parents[1]))

from assemble_nationale.service import AmendementService
from assemble_nationale.parsing.question_parser import parse_question


@click.group()
def cli():
    pass

@cli.command()
@click.argument('id_dossier')
@click.argument('id_examen')
def show_amendements_order(id_dossier, id_examen):
    results = AmendementService().get_amendement_order(id_dossier, id_examen)
    print 'Nombre d\'amendements   : %s' % (len(results),)
    print 'Ordre des ammendements : %s' % (','.join(results),)


@cli.command()
@click.argument('url')
def parse_question_from_url(url):
    question_html = requests.get(url).content
    parsed_data = parse_question(url, question_html)
    print json.dumps(parsed_data, indent=4)


if __name__ == '__main__':
    cli()

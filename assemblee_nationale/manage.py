# -*- coding: utf-8 -*-

import sys
import json

import click
import requests
from pathlib import Path


sys.path.append(str(Path(__file__).absolute().parents[1]))

from assemblee_nationale.service import AmendementSummaryService
from assemblee_nationale.parsing.question_parser import parse_question
from assemblee_nationale.parsing.amendement_parser import parse_amendement


@click.group()
def cli():
    pass


@cli.command()
@click.argument('id_dossier')
@click.argument('id_examen')
def show_amendements_order(id_dossier, id_examen):
    results = AmendementSummaryService().get_amendement_order(id_dossier, id_examen)
    print 'Nombre d\'amendements   : %s' % (len(results),)
    print 'Ordre des ammendements : %s' % (','.join(results),)


@cli.command()
@click.argument('start_date')
@click.option('--end-date')
@click.option('--numero')
def show_amendements(start_date, end_date, numero):
    response = AmendementSummaryService().get_amendements_summary(start_date, end_date=end_date, numero=numero)
    for result in response.results:
        print json.dumps(dict(result._asdict()), indent=4, sort_keys=True, ensure_ascii=False)


@cli.command()
@click.argument('url')
def show_amendement(url):
    print 'Amendement : %s' % url
    print json.dumps(dict((parse_amendement(url, requests.get(url).content)._asdict())), indent=4, sort_keys=True, ensure_ascii=False)


@cli.command()
@click.argument('url')
def show_question(url):
    question_html = requests.get(url).content
    parsed_data = parse_question(url, question_html)
    print json.dumps(parsed_data, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    cli()

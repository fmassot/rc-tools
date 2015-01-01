# -*- coding: utf-8 -*-

import codecs
import sys

import click
from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parents[1]))

from assemblee_nationale.service import AmendementService
from nosdeputes.repository import AmendementRepository


@click.group()
def cli():
    pass

@cli.command()
@click.argument('texteloi_id')
@click.argument('output_filename')
def make_liasse(texteloi_id, output_filename):
    amendements = AmendementRepository().get_by_texteloi_id(texteloi_id)

    with codecs.open(output_filename, 'w', encoding="utf-8") as file:
        file.write(u'Projet de Loi n° %s\n' % texteloi_id)
        file.write(u'%s amendements\n' % len(amendements))

        for amendement in amendements:
            file.write(u'   %s -- %s -- de %s\n' % (amendement.numero, amendement.sujet, amendement.signataires))
            file.write(u'     %s\n' % (amendement.texte,))
            file.write(u'     EXPOSE : %s\n' % (amendement.expose,))


@cli.command()
@click.argument('start_date')
@click.option('--end-date')
@click.option('--size', type=int, default=1000)
def check_if_amendement_are_in_db(start_date, end_date, size):
    amdt_repository = AmendementRepository()
    service = AmendementService()

    print u'Nombre total d\'amendement à checker : %s' % service.get_total_count(start_date, end_date=end_date)

    amendements_summary_iterator = service.iter_on_amendements_summary(start_date, end_date=end_date, size=size)

    for amendements_summary in amendements_summary_iterator:
        print "Page %s / %s" % (amendements_summary.start / size, amendements_summary.total_count / size)
        urls = [a.urlAmend for a in amendements_summary.amendements]
        urls_in_db = [a.source for a in amdt_repository.find_by_url(urls)]
        missing_urls = set(urls) - set(urls_in_db)

        for missing_url in missing_urls:
            print u'Amendement manquant : %s' % missing_url


if __name__ == '__main__':
    cli()

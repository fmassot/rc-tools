# -*- coding: utf-8 -*-

import codecs
import sys

import click
from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parents[1]))

from assemblee_nationale.service import AmendementService
from nosdeputes.model import Amendement


@click.group()
def cli():
    pass

@cli.command()
@click.argument('texteloi_id')
@click.argument('output_filename')
def make_liasse(texteloi_id, output_filename):
    query = Amendement.select().where(Amendement.texteloi_id == texteloi_id)

    with codecs.open(output_filename, 'w', encoding="utf-8") as file:
        file.write(u'Projet de Loi n° %s\n' % texteloi_id)
        file.write(u'%s amendements\n' % query.count())

        for amendement in query:
            file.write(u'   %s -- %s -- de %s\n' % (amendement.numero, amendement.sujet, amendement.signataires))
            file.write(u'     %s\n' % (amendement.texte,))
            file.write(u'     EXPOSE : %s\n' % (amendement.expose,))


@cli.command()
@click.argument('start_date')
@click.option('--end-date')
@click.option('--size', type=int, default=1000)
@click.option('--output-file', default="missing_urls.txt")
def check_if_amendement_are_in_db(start_date, end_date, size, output_file):
    service = AmendementService()

    print u'Nombre total d\'amendement à checker : %s' % service.get_total_count(start_date, end_date=end_date)

    amendements_summary_iterator = service.iter_on_amendements_summary(start_date, end_date=end_date, size=size)

    all_missing_urls = []

    for amendements_summary in amendements_summary_iterator:
        print "Page %s / %s" % (amendements_summary.start / size, amendements_summary.total_count / size)
        urls = [a.url for a in amendements_summary.results]
        urls_in_db = [a.source for a in Amendement.select().where(Amendement.source << urls)]
        missing_urls = set(urls) - set(urls_in_db)

        for missing_url in missing_urls:
            print u'Amendement manquant : %s' % missing_url

        all_missing_urls += list(missing_urls)

    print u'Nombre total d\'amendements manquants : %s' % len(all_missing_urls)

    with open(output_file, 'w') as f:
        f.write('\n'.join(all_missing_urls))


if __name__ == '__main__':
    cli()

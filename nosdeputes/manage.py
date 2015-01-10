# -*- coding: utf-8 -*-

import codecs
import sys

from pathlib import Path


sys.path.append(str(Path(__file__).absolute().parents[1]))

import click

from peewee import SQL
from assemblee_nationale.service import AmendementSearchService, QuestionSearchService
from nosdeputes.model import Amendement, QuestionEcrite
from nosdeputes.parsing.amendement_parsing import amendement_hash


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
@click.option('--start-date')
@click.option('--end-date')
@click.option('--size', type=int, default=1000)
@click.option('--output-file', default="missing_amendement_urls.txt")
def check_if_amendement_are_in_db(start_date, end_date, size, output_file):
    service = AmendementSearchService()

    print u'Nombre total d\'amendement à checker : %s' % service.total_count(start_date=start_date, end_date=end_date)

    amendements_summary_iterator = service.iter(start_date=start_date, end_date=end_date, size=size)

    all_missing_urls = []

    for amendements_summary in amendements_summary_iterator:
        print "Page %s / %s" % (amendements_summary.start / size, amendements_summary.total_count / size)
        amendement_hashes = [amendement_hash(a.url) for a in amendements_summary.results]
        sql_amendement_hash = SQL('CONCAT(legislature, texteloi_id, numero)')
        db_amendement_hashes = [unicode(a.hash) for a in Amendement.select(sql_amendement_hash.alias('hash')).where(sql_amendement_hash << amendement_hashes)]
        missing_amendement_hashes = set(amendement_hashes) - set(db_amendement_hashes)
        missing_urls = [a.url for a in amendements_summary.results if amendement_hash(a.url) in missing_amendement_hashes]
        for missing_url in missing_urls:
            print u'Amendement manquant : %s' % missing_url

        all_missing_urls += list(missing_urls)

    print u'Nombre total d\'amendements manquants : %s' % len(all_missing_urls)

    with open(output_file, 'w') as f:
        f.write('\n'.join(all_missing_urls))


@cli.command()
@click.option('--legislature', type=int, default=14)
@click.option('--is-removed', type=bool, default=None)
@click.option('--is-answered', type=bool, default=None)
@click.option('--size', type=int, default=1000)
@click.option('--output-file', default="missing_question_urls.txt")
def check_if_questions_are_in_db(legislature, is_removed, is_answered, size, output_file):
    service = QuestionSearchService()

    print u'Nombre total de questions à checker : %s' % service.total_count(legislature=legislature, is_answered=is_answered, is_removed=is_removed)

    search_iterator = service.iter(legislature=legislature, is_answered=is_answered, is_removed=is_removed, size=size)

    all_missing_urls = []

    for i, search_result in enumerate(search_iterator):
        print "Page %s / %s" % (i, search_result['total_count'] / size)
        question_urls = map(lambda q: q['url'], search_result['results'])
        db_question_urls = [q.source for q in QuestionEcrite.select().where(QuestionEcrite.source << question_urls)]
        missing_urls = set(question_urls) - set(db_question_urls)
        for missing_url in missing_urls:
            print u'Question manquante : %s' % missing_url

        all_missing_urls += list(missing_urls)

    print u'Nombre total de questions manquantes : %s' % len(all_missing_urls)

    with open(output_file, 'w') as f:
        f.write('\n'.join(all_missing_urls))

if __name__ == '__main__':
    cli()

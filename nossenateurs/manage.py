# -*- coding: utf-8 -*-

import click
import sys

from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parents[1]))

from senapy.service import QuestionSearchService
from nossenateurs.models import Question


@click.group()
def cli():
    pass


@cli.command()
@click.option('--start-date')
@click.option('--end-date')
@click.option('--output-file', default="missing_questions_urls.txt")
def check_if_questions_are_in_db(start_date, end_date, output_file):
    service = QuestionSearchService()

    params = {'de': start_date, 'au': end_date}

    total_count = service.total_count(params)

    print u'Nombre total de question à checker : %s' % total_count

    all_missing_urls = []

    for i, search_result in enumerate(service.iter(params)):
        print "Page %s / %s" % (i, total_count / 10)

        urls = [r.url for r in search_result.results]

        db_urls = [q.source for q in Question.select(Question.source).where(Question.source << urls)]

        missing_urls = set(urls) - set(db_urls)
        all_missing_urls += list(missing_urls)

        for missing_url in missing_urls:
            print u'Questions manquantes : %s' % missing_url

    print u'Nombre total de questions manquantes : %s' % len(all_missing_urls)

    with open(output_file, 'w') as f:
        f.write('\n'.join(all_missing_urls))


if __name__ == '__main__':
    cli()

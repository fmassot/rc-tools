# -*- coding: utf-8 -*-

import click
import codecs
import re
import sys

from pathlib import Path
from peewee import SQL

sys.path.append(str(Path(__file__).absolute().parents[1]))

from nossenateurs.senpy.service import QuestionSearchService
from nossenateurs.models import Question


@click.group()
def cli():
    pass


@cli.command()
@click.option('--start-date')
@click.option('--end-date')
@click.option('--output-file', default="missing_questions_urls.txt")
def check_if_qag_are_in_db(start_date, end_date, output_file):
    service = QuestionSearchService()

    params = {'de': start_date, 'au': end_date}

    total_count = service.total_count(params)

    print u'Nombre total de question à checker : %s' % total_count

    all_missing_urls = []

    urls = [q.source for q in Question.select(Question.source).where(Question.type == u"Question d'actualité au gouvernement", Question.legislature == 14)]

    for i, search_result in enumerate(service.iter(params)):
        print "Page %s / %s" % (i, total_count / 10)

        for result in search_result.results:
            if result.url not in urls:
                print result

    with open(output_file, 'w') as f:
        f.write('\n'.join(all_missing_urls))


if __name__ == '__main__':
    cli()

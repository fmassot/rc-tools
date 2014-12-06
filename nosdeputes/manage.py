# -*- coding: utf-8 -*-

import codecs
import click
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parents[1]))

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
            file.write(u'   %s -- %s -- de %s\n' % (amendement['numero'], amendement['sujet'], amendement['signataires']))
            file.write(u'     %s\n' % (amendement['texte'],))
            file.write(u'     EXPOSE : %s\n' % (amendement['expose'],))


if __name__ == '__main__':
    cli()

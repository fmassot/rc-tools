# -*- coding: utf-8 -*-

import click
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parents[1]))

from assemble_nationale.service import AmendementService


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


if __name__ == '__main__':
    cli()

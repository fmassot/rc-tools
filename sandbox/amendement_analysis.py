# -*- coding: utf-8 -*-
import sys

from pathlib import Path


sys.path.append(str(Path(__file__).absolute().parents[1]))

import pandas

from bokeh.plotting import output_file, figure, show

from nosdeputes.api import NDApi


def analyze_amendement():
    api = NDApi()

    df = pandas.DataFrame(api.synthese())

    colormap = {
        u'UMP': '#0000CD',
        u'ECOLO': '#32CD32',
        u'SRC': '#FF69B4',
        u'NI': 'grey',
        u'GDR': '#DC143C',
        u'UDI': '#87CEFA',
        u'RRDP': '#FFFF00',
    }

    df['colors'] = df.groupe_sigle.map(lambda x: colormap[x])

    print df.describe()

    output_file('amendement_analysis.html', title=u'Analyse amendement')

    p = figure(title=u'Amendement')
    p.xaxis.axis_label = u'Signé'
    p.yaxis.axis_label = u'Adopté'

    p.scatter(df.amendements_signes, df.amendements_adoptes, color=df.colors, fill_alpha=0.6, size=10)

    show(p)


if __name__ == '__main__':
    analyze_amendement()
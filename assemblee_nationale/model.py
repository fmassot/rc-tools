# -*- coding: utf-8 -*-

from collections import namedtuple


Amendement = namedtuple(
    'Amendement',
    [
        'url', 'num_amtxt', 'amend_parent', 'url_dossier', 'num_init', 'etape', 'deliberation', 'titre_init',
        'num_partie', 'designation_article', 'url_division', 'designation_alinea', 'mission', 'auteurs', 'auteur_id',
        'groupe_id', 'cosignataires_id', 'seance', 'sort', 'date_badage', 'date_sort', 'ordre_texte', 'code', 'refcode',
        'legislature', 'dispositif', 'expose',
    ]
)

AmendementSummary = namedtuple(
    'AmendementSummary',
    [
        'id', 'num_init', 'titre_init', 'url_dossier', 'instance', 'num_amtxt', 'url',
        'designation_article', 'designation_alinea', 'date_depot', 'signataires', 'sort', 'legislature'
    ]
)


AmendementSummaryResponse = namedtuple(
    'AmendementSummaryResponse',
    ['url', 'total_count', 'start', 'size', 'results']
)

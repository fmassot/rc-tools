# -*- coding: utf-8 -*-

from enum import Enum


class SortAmendement(Enum):
    adopted = u'Adopté'
    rejected = u'Rejeté'
    not_supported = u'Non soutenu'
    undefined = u'Indéfini'
    corrected = u'Rectifié'
    removed = u'Retiré'
    fallen = u'Tombe'
    removed_before_seance = u'Retiré avant séance'
    unacceptable = u'Irrecevable'
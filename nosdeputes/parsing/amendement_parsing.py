# -*- coding: utf-8 -*-

import datetime
import re

from nosdeputes.constant import SortAmendement


def amendement_hash(url):
    try:
        legislature, TA, texteloi_id, part_loi, something, num_am = re.search('/(\d+)/amendements/(TA)?(\d+)([A-z]+)?/([\w-]+)/(\w+)\.asp', url).groups()
        part_loi = '' if part_loi is None else part_loi
        texteloi_id = str(int(texteloi_id))
        texteloi_id = 'TA' + texteloi_id if TA else texteloi_id
        hash = unicode(legislature + texteloi_id + num_am + part_loi)
    except:
        print url
        print legislature, texteloi_id, part_loi, something, num_am
        raise
    return hash


def parse_amendement_sort(sort):
    sort = sort.lower()

    if sort == u'irrecevable':
        return SortAmendement.unacceptable.value
    elif re.search(u'retir.+(s.+ance|publication)', sort):
        return SortAmendement.removed_before_seance.value
    elif sort == u'retiré':
        return SortAmendement.removed.value
    elif re.search(u'non.*(soutenu,défendu)', sort):
        return SortAmendement.not_supported.value
    elif sort == u'tombé':
        return SortAmendement.fallen.value
    elif sort == u'rejeté':
        return SortAmendement.rejected.value
    elif sort == u'adopté':
        return SortAmendement.adopted.value
    else:
        raise Exception('Sort amendement inconnu : %s' % sort)


def parse_rectif(num):
    return 1 if re.search(u'\w+\s\(Rect\)', num) else 0


def parse_date(date):
    return datetime.datetime.strptime(date, '%d/%m/%Y').date()


def parse_num(num):
    return re.search(u'(\w+)\s\(Rect\)?', num).group(1)
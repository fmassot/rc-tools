# -*- coding: utf-8 -*-

from addict import Dict
import datetime
import re

from nosdeputes.constant import SortAmendement


def amendement_hash(url):
    parsed_data = parse_amendement_url(url)
    return parsed_data.legislature + parsed_data.texteloi_id + parsed_data.numero


def parse_amendement_url(url):
    legislature, prefix_loi_id, loi_id, loi_ABCD, commission, prefix_am_number, am_number = \
        re.search('/(\d+)/amendements/([A-z]+)?(\d+)([A-z]+)?/([\w-]+)/([A-z]+)?(\d+)\.asp', url).groups()

    prefix_am_number = '' if prefix_am_number is None else prefix_am_number
    loi_ABCD = '' if loi_ABCD is None else loi_ABCD

    # Set prefix when this is a commission and when there is not already a prefix
    if commission != 'AN' and not prefix_am_number:
        prefix_am_number = commission

    # remove the first '0' digits
    loi_id = str(int(loi_id))
    loi_id = prefix_loi_id + loi_id if prefix_loi_id else loi_id

    return Dict(legislature=legislature, texteloi_id=loi_id, numero=prefix_am_number + am_number + loi_ABCD)


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
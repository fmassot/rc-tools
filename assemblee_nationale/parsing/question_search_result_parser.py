# -*- coding: utf-8 -*-

import re

from bs4 import BeautifulSoup


def parse_question_search_result(url, html_content):
    soup = BeautifulSoup(html_content)

    data = {
        'total_count': int(soup.find('article').div.div.p.strong.text)
    }

    results = []
    for tr in soup.find_all('tr')[1:]:
        url = tr.td.a['href']
        legislature, numero = re.search('(\d+)-(\d+)QE\.htm', url).groups()
        question_info_td = tr.find_all('td')[1]
        results.append({
            'url': url,
            'legislature': legislature,
            'numero': numero,
            'auteur': question_info_td.strong.text,
            'tags': question_info_td.em.text
        })

    data['results'] = results
    data['next_url'] = soup.find('div', class_='pagination-bootstrap').find_all('li')[-1].a['href']

    return data
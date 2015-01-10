# -*- coding: utf-8 -*-

import re

from bs4 import BeautifulSoup


def parse_question_search_result(url, html_content):
    soup = BeautifulSoup(html_content)

    data = {
        'url': url,
        'total_count': int(soup.find('article').div.div.p.strong.text)
    }

    results = []
    for tr in soup.find_all('tr')[1:]:
        all_tds = tr.find_all('td')
        url = all_tds[0].a['href']
        legislature, numero, question_type = re.search('(\d+)-(\d+)(QE|QOSD)\.htm', url).groups()
        dates = all_tds[2].find_all('strong')
        results.append({
            'url': url,
            'legislature': legislature,
            'numero': numero,
            'question_type': question_type,
            'auteur': all_tds[1].strong.text,
            'tags': all_tds[1].em.text,
            'publication_date': dates[0].text,
            'answer_date': dates[1].text if len(dates) > 1 else None,
        })

    data['results'] = results
    next_link = soup.find('div', class_='pagination-bootstrap').find_all('li')[-1]
    data['next_url'] = next_link.a['href'] if next_link.a else None

    return data
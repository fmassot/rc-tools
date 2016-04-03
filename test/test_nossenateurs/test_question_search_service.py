# -*- coding: utf-8 -*-

from nossenateurs.senpy.service import QuestionSearchService


def test_service():
    service = QuestionSearchService()
    iterator = service.iter()
    search_result = iterator.next()

    assert 330 == search_result.total_count
    assert 10 == search_result.size


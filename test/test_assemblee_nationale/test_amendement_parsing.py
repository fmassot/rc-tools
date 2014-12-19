# -*- coding: utf-8 -*-

import unittest

from assemblee_nationale.parsing.amendement_parser import parse_amendement_json_response


class AmendementParsingTest(unittest.TestCase):
    def test_question_parsing(self):
        json_response = {
            u'data_table': [
                u"S-AMANR5L14PO59051B996N4|996|Justice : d\xe9ch\xe9ance de la nationalit\xe9 pour tout individu portant les armes contre l'arm\xe9e et la police|http://www.assemblee-nationale.fr/14/dossiers/decheance_nationalite_contre_armees_police.asp|Lois|CL4|http://www.assemblee-nationale.fr/14/amendements/0996/CION_LOIS/CL4.asp|Article UNIQUE||21 novembre 2014|M. Coronado et M. Molac|Adopt\xe9",
                u"S-AMANR5L14PO59051B996N1|996|Justice : d\xe9ch\xe9ance de la nationalit\xe9 pour tout individu portant les armes contre l'arm\xe9e et la police|http://www.assemblee-nationale.fr/14/dossiers/decheance_nationalite_contre_armees_police.asp|Lois|CL1|http://www.assemblee-nationale.fr/14/amendements/0996/CION_LOIS/CL1.asp|Article UNIQUE||21 novembre 2014|M. Meunier, rapporteur|Tomb\xe9",
            ],
            u'infoGenerales': {
                u'debut': 1,
                u'description_schema': u'id|numInit|titreDossierLegislatif|urlDossierLegislatif|instance|numAmend|urlAmend|designationArticle|designationAlinea|dateDepot|signataires|sort',
                u'nb_docs': 2500,
                u'nb_resultats': 6123,
                u'schema': u'partiel'
            }
        }

        expected_result = {
            u'id': u'S-AMANR5L14PO59051B996N4',
            u'numInit': u'996',
            u'titreDossierLegislatif': u"Justice : d\xe9ch\xe9ance de la nationalit\xe9 pour tout individu portant les armes contre l'arm\xe9e et la police",
            u'urlDossierLegislatif': u'http://www.assemblee-nationale.fr/14/dossiers/decheance_nationalite_contre_armees_police.asp',
            u'instance': u'Lois',
            u'numAmend': u'CL4',
            u'urlAmend': u'http://www.assemblee-nationale.fr/14/amendements/0996/CION_LOIS/CL4.asp',
            u'designationArticle': u'Article UNIQUE',
            u'designationAlinea': u'',
            u'dateDepot': u'21 novembre 2014',
            u'signataires': u'M. Coronado et M. Molac',
            u'sort': u'Adopt\xe9',
        }

        amendements = parse_amendement_json_response(json_response)

        self.assertDictEqual(expected_result, amendements[0].to_dict())

if __name__ == '__main__':
    unittest.main()
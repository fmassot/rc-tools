# -*- coding: utf-8 -*-

import requests
import unittest

from assemblee_nationale.parsing.amendement_parser import parse_amendements_json_response, parse_amendement_html


class AmendementParsingTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_json_parsing(self):
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
            u'legislature': u'14',
            u'texteloi_id': u'0996',
        }

        amendements = parse_amendements_json_response(json_response)

        self.assertDictEqual(expected_result, amendements[0].to_dict())

    def test_html_parsing(self):
        parsing_result = parse_amendement_html(
            requests.get("http://www.assemblee-nationale.fr/14/amendements/0996/CION_LOIS/CL4.asp").content
        )

        expected_result = {
            u'amendParent': u'',
            u'auteurId': u'610860',
            u'auteurs': u' M. Coronado et M. Molac',
            u'code': u'',
            u'cosignataireIds': u'607619',
            u'date_badage': u'24/11/2014',
            u'date_sort': u'26/11/2014',
            u'deliberation': u'',
            u'designationAlinea': u'',
            u'designationArticle': u'ART. UNIQUE',
            u'dispositif': u'\nSupprimer cet article.\n',
            u'etape': u'1ère lecture (1ère assemblée saisie)',
            u'expose': u"\nLa présente proposition de loi souhaite permettre la déchéance de nationalité à toute personne portant les armes contre les forces armées françaises et de police, ou leurs alliés.\nActuellement la loi prévoit déjà la possible de déchoir de leur nationalité française les personnes condamnées pour un crime ou délit constituant une atteinte aux intérêts fondamentaux de la nation et les personnes condamnées, en France ou à l'étranger, pour crime à au moins cinq années d'emprisonnement.\nAu-delà de son affichage, la présente proposition de loi ne couvrirait pas de cas nouveaux. Elle vise surtout à supprimer des garanties essentielles.\nComme le propose le rapporteur, l’avis du Conseil d’Etat resterait systématique, mais il ne serait plus obligatoirement suivi. C’est pourtant une garantie fondamentale. La garantie temporelle prévu à l’article 25-1 du code civil serait également abrogée.\nIl est à noter que la proposition de loi vise les personnes ayant acquis la nationalité française. Il est pourtant dangereux de considérer qu’il y aurait plusieurs catégories de citoyens.\nLes récentes affaires montrent également que le problème de « djihaddistes français » n’est pas un problème de binationaux, ou de personnes qui auraient acquis la nationalité française.\nPour toutes ces raisons, il est proposé de supprimer l’article unique de cette loi.\n",
            u'groupeId': u'656014',
            u'legislature': u'14',
            u'mission': u'',
            u'numAmend': u'CL4',
            u'numInit': u'996',
            u'numPartie': u'',
            u'ordre_texte': u'eaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac',
            u'refcode': u'',
            u'seance': u'',
            u'sort': u'Adopté',
            u'titreDossierLegislatif': u'DÉCHÉANCE DE NATIONALITÉ POUR LES ATTEINTES AUX FORCES ARMÉES ET DE POLICE(n°996)',
            u'urlDivision': u'/14/textes/0996.asp#D_Article_unique',
            u'urlDossier': u'http://www.assemblee-nationale.fr/14/dossiers/decheance_nationalite_contre_armees_police.asp'
        }

        self.assertDictEqual(expected_result, parsing_result.to_dict())

if __name__ == '__main__':
    unittest.main()
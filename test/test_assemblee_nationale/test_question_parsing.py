# -*- coding: utf-8 -*-

import unittest
import requests
from assemblee_nationale.parsing.question_parser import parse_question


class QuestionParsingTest(unittest.TestCase):
    def test_question_parsing(self):
        expected_result = {"source": "http://questions.assemblee-nationale.fr/q14/14-67716QE.htm", "legislature": "14", "type": "QE", "numero": "67716", "date_question": "2014-10-28", "date_retrait": "", "date_reponse": "", "date_signalement": "", "date_cht_attr": "", "page_question": "8856", "page_reponse": "", "ministere_attribue": "Affaires sociales, santé et droits des femmes", "ministere_interroge": "Affaires sociales, santé et droits des femmes", "tete_analyse": "soins palliatifs", "analyse": "formation universitaire", "rubrique": "santé", "question": "Mme Michèle Delaunay attire l'attention de Mme la ministre des affaires sociales, de la santé et des droits des femmes sur la création d'une filière universitaire de médecine palliative. Il existe aujourd'hui en France 120 unités de soins palliatifs, 350 équipes mobiles de soins palliatifs et 4 000 lits identifiés de soins palliatifs ; pourtant, aucune filière de médecine palliative ne prépare spécifiquement les médecins et équipes soignantes à ce domaine qui est amené à se développer dans les années à venir. Des diplômes d'études spécialisées (DES) « urgence » et « gériatrie » vont être prochainement créés et pour les professionnels qui exercent dans les soins palliatifs, il est important que voit le jour également un DES « médecine palliative » pour répondre à un véritable besoin. Il est important de prendre en compte le fait que les « baby » boomers entrent aujourd'hui dans le champ de l'âge et qu'on prévoit que le nombre de décès annuel, parfaitement stable depuis 1950, va augmenter de 50 % d'ici 2050, amenant un développement considérable du besoin d'accompagnement de la fin de vie. Elle lui demande donc ce que le Gouvernement entend mettre en place pour permettre le développement de cette filière majeure pour cet accompagnement de la fin de vie.", "reponse": "", "motif_retrait": "", "auteur": "Michèle Delaunay"}

        data = requests.get(expected_result['source']).content
        parsing_result = parse_question(expected_result['source'], data)

        self.assertDictEqual(expected_result, parsing_result)


if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-

import datetime
import unittest

from assemblee_nationale.service import AmendementService
from nosdeputes.mapping.an_mapping import an_to_nd_amendement_mapper


class ANMappingTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_amendement_1(self):

        an_amendement = AmendementService().get_amendement("http://www.assemblee-nationale.fr/14/amendements/2455/AN/76.asp")
        amendement = an_to_nd_amendement_mapper(an_amendement)

        self.assertEquals('http://www.assemblee-nationale.fr/14/amendements/2455/AN/76.asp', amendement.source)
        self.assertEquals('14', amendement.legislature)
        self.assertEquals('2455', amendement.texteloi_id)
        self.assertEquals('76', amendement.numero)
        self.assertEquals('46', amendement.sous_amendement_de)
        self.assertEquals(1, amendement.rectif)
        self.assertEquals(u'ART. 16', amendement.sujet)
        self.assertEquals(u'Retiré', amendement.sort)
        self.assertEquals(datetime.date(2014, 12, 16), amendement.date)
        self.assertEquals('Mme Rabault', amendement.signataires)

        # Three diffs with whats in db :
        #  * Abis instead of A bis
        #  * Bsexies instead of B sexies
        #  * no space after a comma instead of a space after
        self.assertEquals(
            u"<p>I.- Rédiger ainsi les alinéas 4 et 5 :</p><p>« B. – Après l'article 1407 bis, il est inséré un article 1407 ter ainsi rédigé :</p><p>« Art. 1407 ter – Dans les communes classées dans les zones géographiques mentionnées au premier alinéa du I de l'article 232, pour la taxe d'habitation due au titre des logements meublés non affectés à l'habitation principale, le conseil municipal peut, par une délibération prise dans les conditions prévues à l'article 1639 A bis, majorer son taux de taxe d'habitation dans la limite de 20 %. Cette majoration n'est pas prise en compte pour l'application des articles 1636 B sexies et 1636 Bdecies. ».</p><p>II. – En conséquence, à l'alinéa 11, substituer aux mots :</p><p>« au 4 du I de l'article 1636 B sexies »,</p><p>les mots :</p><p>« à l'article 1407 ter ».</p>",
            amendement.texte
        )

        self.assertEquals(
            u"<p>Le présent amendement vise à codifier séparément la modulation du taux de la taxe d'habitation au titre des résidences secondaires.</p>",
            amendement.expose
        )


if __name__ == '__main__':
    unittest.main()
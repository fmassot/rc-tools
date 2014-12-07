# -*- coding: utf-8 -*-


class Amendement(object):
    def __init__(self, id=None, nb_commentaires=None, source=None, legislature=None, texteloi_id=None, numero=None,
                 sous_amendement_de=None, rectif=None, sujet=None, sort=None, date=None, signataires=None, texte=None,
                 expose=None, content_md5=None, nb_multiples=None, created_at=None, updated_at=None):
        self.id = id
        self.nb_commentaires = nb_commentaires
        self.source = source
        self.legislature = legislature
        self.texteloi_id = texteloi_id
        self.numero = numero
        self.sous_amendement_de = sous_amendement_de
        self.rectif = rectif
        self.sujet = sujet
        self.sort = sort
        self.date = date
        self.signataires = signataires
        self.texte = texte
        self.expose = expose
        self.content_md5 = content_md5
        self.nb_multiples = nb_multiples
        self.created_at = created_at
        self.udpated_at = updated_at


class Parlementaire(object):
    def __init__(self, id=None, nb_commentaires=None, nom=None, nom_de_famille=None, sexe=None, date_naissance=None, lieu_naissance=None,
                 nom_circo=None, num_circo=None, sites_web=None, debut_mandat=None, fin_mandat=None, place_hemicycle=None, url_an=None,
                 profession=None, autoflip=None, id_an=None, type=None, groupe_acronyme=None, parti=None, adresses=None, suppleant_de_id=None,
                 anciens_mandats=None, autres_mandats=None, anciens_autres_mandats=None, mails=None, top=None, villes=None, url_ancien_cpc=None,
                 url_nouveau_cpc=None, created_at=None, updated_at=None, slug=None):
        self.id = id
        self.nb_commentaires = nb_commentaires
        self.nom = nom
        self.nom_de_famille = nom_de_famille
        self.sexe = sexe
        self.date_naissance = date_naissance
        self.lieu_naissance = lieu_naissance
        self.nom_circo = nom_circo
        self.num_circo = num_circo
        self.sites_web = sites_web
        self.debut_mandat = debut_mandat
        self.fin_mandat = fin_mandat
        self.place_hemicycle = place_hemicycle
        self.url_an = url_an
        self.profession = profession
        self.autoflip = autoflip
        self.id_an = id_an
        self.type = type
        self.groupe_acronyme = groupe_acronyme
        self.parti = parti
        self.adresses = adresses
        self.suppleant_de_id = suppleant_de_id
        self.anciens_mandats = anciens_mandats
        self.autres_mandats = autres_mandats
        self.anciens_autres_mandats = anciens_autres_mandats
        self.mails = mails
        self.top = top
        self.villes = villes
        self.url_ancien_cpc = url_ancien_cpc
        self.url_nouveau_cpc = url_nouveau_cpc
        self.created_at = created_at
        self.updated_at = updated_at
        self.slug = slug
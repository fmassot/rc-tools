# -*- coding: utf-8 -*-

from peewee import *

database = PostgresqlDatabase('dosleg', **{})


class UnknownField(object):
    pass


class BaseModel(Model):
    class Meta:
        database = database


class Ass(BaseModel):
    """
    Assemblée

    A      | Assemblée nationale
    S      | Sénat
    I      | Indéterminé
    """
    codass = CharField(primary_key=True)
    libass = CharField()

    class Meta:
        db_table = 'ass'


class Aud(BaseModel):
    """
    Audition
    """
    audcle = BigIntegerField(primary_key=True)
    auddat = DateTimeField()
    audtit = CharField()
    audurl = CharField()
    lecassidt = CharField(index=True)
    orgcod = CharField(index=True)

    class Meta:
        db_table = 'aud'


class Auteur(BaseModel):
    autcod = CharField(primary_key=True)
    autfct = CharField(null=True) # info ministre
    autmat = CharField(index=True, null=True)
    datdeb = DateTimeField(null=True)
    datfin = DateTimeField(null=True)
    grpapp = CharField(null=True)
    grprat = CharField(null=True)
    nomtec = CharField()
    nomuse = CharField()
    prenom = CharField(null=True)
    quacod = CharField()
    senfem = CharField(null=True)
    typautcod = CharField(index=True)

    class Meta:
        db_table = 'auteur'


class Ble(BaseModel):
    """
     00001  | Education nationale
     00002  | Affaires étrangères
     00003  | Agriculture et pêche
     00004  | Anciens combattants
     00006  | Charges communes
     00009  | Comptes spéciaux du trésor
     00010  | Culture
     00013  | Défense
     00014  | Economie, finances et industrie
     00015  | Emploi et solidarité
     00018  | Aménagement du territoire et environnement
     00019  | Equipement, transports et logement
     00020  | Fonction publique et réforme de l'Etat
     00022  | Intérieur et décentralisation
     00023  | Jeunesse et sports
     00024  | Justice
     00028  | Outre-mer
     00030  | Ports maritimes
     00033  | Recherche
     00043  | Services du premier ministre
     00044  | Tourisme
     00045  | Aménagement du territoire, logement et environnement
     00046  | Equipements et transports
     132    | Budgets annexes
    """
    blecod = CharField(primary_key=True)
    blelib = CharField(index=True)

    class Meta:
        db_table = 'ble'


class Bur(BaseModel):
    """
    Fonction au sein du bureau

      burcod   |         burlib
    -----------+-------------------------
     AUCUNSEN  |
     PDTSEN    | Président du Sénat
     QUESTESEN | Questeur du Sénat
     SECRETSEN | Secrétaire du Sénat
     VICPDTSEN | Vice-président du Sénat
    """
    burcod = CharField(primary_key=True)
    burlib = CharField(null=True)
    burlibfem = CharField(null=True)
    burlibfemplu = CharField(null=True)
    burlibhon = CharField(null=True)
    burlibhonfem = CharField(null=True)
    burlibhonplu = CharField(null=True)
    burlibplu = CharField(null=True)
    burlic = CharField(null=True)
    burlicfem = CharField(null=True)
    burlicfemplu = CharField(null=True)
    burlicplu = CharField(null=True)
    burlil = CharField(null=True)
    burlilfem = CharField(null=True)
    burlilfemplu = CharField(null=True)
    burlilplu = CharField(null=True)
    burnumtri = BigIntegerField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)

    class Meta:
        db_table = 'bur'


class Catrap(BaseModel):
    """
     P         | Rapport parlementaire
     E         | Etude
     R         | Document de référence
     C         | Actes de colloques
    """
    catrapcod = CharField(primary_key=True)
    catraplib = CharField()

    class Meta:
        db_table = 'catrap'


class TyporgSen(BaseModel):
    """
      typorgcod  |                                   typorglib
    -------------+--------------------------------------------------------------------------------
     COMITE      | Comité
     AUCUN       | (aucun)
     AUTRES      | Autres organismes
     COM         | Commission permanente
     DELEGA      | Délégation
     ETUDES      | Groupe d'études
     GRPSEN      | Groupe interparlementaire d'amitié
     OFFICE      | Office parlementaire
     ORGEXT      | Organisme Extra-Parlementaire
     CONEUR      | Conseil de l'Europe et UEO
     GRPPOL      | Groupe politique
     COUJUSREP   | Cour de Justice de la République
     SENAT       | Sénat
     CONCST      | Conseil Constitutionnel
     BUR         | Bureau du Sénat
     MINIST      | Ministère
     COMENQ      | Commission d'enquête
     MISINF      | Mission d'information
     MISINFCOM   | Mission commune d'information
     PARPOL      | Parti politique
     COMPOU      | Commission de poursuite
     COMADHOC    | Commission ad'hoc
     CMP         | Commission mixte paritaire
     ETUDESSCN   | Section d'un groupe d'études
     OBS         | Observatoire
     COMEUR      | Commission européenne
     MISCOM      | Mission commune
     MECSS       | Mission d'évaluation et de contrôle de la sécurité sociale
     GRPSENSCN   | Section d'un Groupe interparlementaire d'amitié
     CSCE        | Conférence sur la sécurité et la coopération en Europe
     GRPPOLNI    | Groupe politique des Non Inscrits
     COMSPE      | Commission spéciale
     HAUCOUJUS   | Haute Cour de Justice
     COMSPEAPU   | Commission spéciale chargée du contrôle des comptes et de l'évaluation interne
     COMAPLEG    | Commission en charge de l'application des lois
     COMSENCOMMU | Commission du Sénat de la Communauté
     GRPLIAISON  | Groupe de liaison
    """
    evetempub = CharField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    typorgcod = CharField(primary_key=True)
    typorglib = CharField()
    typorglibplu = CharField(null=True)
    typorglic = CharField()
    typorgnumtri = BigIntegerField(null=True)
    typorgurlcmp = CharField(null=True)
    typorgurlsim = CharField(null=True)

    class Meta:
        db_table = 'typorg_sen'


class Com(BaseModel):
    # Commissions
    comcodameli = CharField(null=True)
    comlibameli = CharField(null=True)
    comlilmin = CharField(null=True)
    divcod = CharField(index=True, null=True)
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    orgart = CharField(null=True)
    orgcod = CharField(primary_key=True)
    orgdatcre = DateTimeField(null=True)
    orgdatfin = DateTimeField(null=True)
    orgnumtie = CharField(null=True)
    orgnumtri = BigIntegerField(null=True)
    orgurlcmp = CharField(null=True)
    orgurlsim = CharField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(null=True)
    typorgcod = ForeignKeyField(db_column='typorgcod', rel_model=TyporgSen, to_field='typorgcod')

    class Meta:
        db_table = 'com'


class Corscr(BaseModel):
    """
    Compte rendu analytique officiel
    257 lignes, c peu
    """
    corscrord = BigIntegerField(null=True)
    corscrtxt = CharField()
    corscrurl = CharField(null=True)
    scrnum = BigIntegerField()
    sesann = BigIntegerField()

    class Meta:
        db_table = 'corscr'
        indexes = (
            (('sesann', 'scrnum'), False),
        )


class DateSeance(BaseModel):
    code = BigIntegerField(primary_key=True)
    date_s = DateTimeField(null=True)
    lecidt = CharField(index=True, null=True)
    statut = CharField(null=True)

    class Meta:
        db_table = 'date_seance'


class Deccoc(BaseModel):
    """
    Avis CC ?

     01        | conforme
     02        | partiellement conforme
     03        | non conforme
     04        | se déclare incompétent
    """
    deccoccod = CharField(primary_key=True)
    deccoclib = CharField()

    class Meta:
        db_table = 'deccoc'


class Delega(BaseModel):
    """
    Délégation :
        - Section française de l'Assemblée parlementaire de la francophonie
        - Groupe français de l'Union Interparlementaire (U.I.P.)
        - Délégation française à l'Assemblée parlementaire de l'OTAN
        - Comité de déontologie parlementaire du Sénat
        - Délégation pour la planification
        - Délégation parlementaire au renseignement
        - Mission d'évaluation et de contrôle de la sécurité sociale
        ...

    """
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    orgart = CharField(null=True)
    orgcod = CharField(primary_key=True)
    orgdatcre = DateTimeField(null=True)
    orgdatfin = DateTimeField(null=True)
    orgmemdep = CharField(null=True)
    orgmoddes = CharField(null=True)
    orgnumtie = CharField(null=True)
    orgnumtri = BigIntegerField(null=True)
    orgregjur = CharField(null=True)
    orgurlcmp = CharField(null=True)
    orgurlsim = CharField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(null=True)
    typorgcod = ForeignKeyField(db_column='typorgcod', rel_model=TyporgSen, to_field='typorgcod')

    class Meta:
        db_table = 'delega'


class Denrap(BaseModel):
    """
    Type de rapports :
        - Avis
        - Rapport d'information
        - Rapport de commission d'enquête
        - Rapport de groupe interparlementaire d'amitié
        ...

    """
    coddenrap = CharField(primary_key=True)
    denrapmin = CharField(null=True)
    denrapstymin = CharField(null=True)
    denraptit = CharField(null=True)
    gencod = CharField()
    libdenrap = CharField()
    ordre = BigIntegerField(null=True)
    solnatrapcod = CharField(index=True, null=True)
    typraprap = CharField(index=True)

    class Meta:
        db_table = 'denrap'


class Designorg(BaseModel):
    """
    Type de membres :
        - Membres
        - Membres titulaires
        - Membres suppléants
        - Membres de droit
        - Membres de droit, commissions
        - Membres désignés par les groupes
    """
    designcod = CharField(primary_key=True)
    designlib = CharField(null=True)
    designlibfem = CharField(null=True)
    designlic = CharField(null=True)
    designlicfem = CharField(null=True)
    designlil = CharField(null=True)
    designlilfem = CharField(null=True)
    designnumtri = BigIntegerField(null=True)
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'designorg'


class Lecture(BaseModel):
    """

    leccom :
        - Nouvelle lecture
        - Commission mixte paritaire (désaccord)
        - Commission mixte paritaire (accord)
        - Commission mixte paritaire (provoquée, le 29 septembre 2009, à l'initiative conjointe des présidents du Sénat et de l'Assemblée nationale)
        - Quatrième lecture
        - Première lecture
        - Deuxième lecture
        - Troisième lecture
        - Commission mixte paritaire
        - Référendum
        - Congrès du Parlement
    """
    leccom = CharField(null=True)
    lecidt = CharField(primary_key=True)
    loicod = CharField(index=True)
    typleccod = CharField()

    class Meta:
        db_table = 'lecture'


class Ses(BaseModel):
    """
    Session
        2006 | 2006-2007
        ...
        2013 | 2013-2014
        ...
    """
    sesann = BigIntegerField(primary_key=True)
    seslib = CharField()

    class Meta:
        db_table = 'ses'


class Typdoc(BaseModel):
    """
    Type de document
        DEC       | décret
        DPO       | document déposé
    """
    typdoccod = CharField(primary_key=True)
    typdoclib = CharField(null=True)

    class Meta:
        db_table = 'typdoc'


class Doc(BaseModel):
    """
    doctitcou :
        - Ce document, déposé à la suite d'une erreur matérielle, n'a pas été publié
        - Déclaration de politique générale du Gouvernement
        - Allocution du Président du Sénat, M. Jean-Pierre BEL
        ...
    """
    date_depot = DateTimeField(null=True)
    docdat = DateTimeField(null=True)
    docdatsea = DateTimeField(null=True)
    docidt = BigIntegerField(primary_key=True)
    docint = CharField(null=True)
    docnum = BigIntegerField(null=True)
    doctitcou = CharField(null=True)
    docurl = CharField(null=True)
    lecidt = ForeignKeyField(db_column='lecidt', null=True, rel_model=Lecture, to_field='lecidt')
    sesann = ForeignKeyField(db_column='sesann', null=True, rel_model=Ses, to_field='sesann')
    typdoccod = ForeignKeyField(db_column='typdoccod', null=True, rel_model=Typdoc, to_field='typdoccod')

    class Meta:
        db_table = 'doc'


class Docatt(BaseModel):
    """
    doc pdf attaché ?
    """
    docattcle = BigIntegerField(primary_key=True)
    docatturl = CharField(null=True)
    rapcod = BigIntegerField(index=True)
    typattcod = CharField(index=True)

    class Meta:
        db_table = 'docatt'


class Docsea(BaseModel):
    docseaord = BigIntegerField(null=True)
    docseaurl = CharField(null=True)
    docseaurlapr = CharField(null=True)
    docseaurlava = CharField(null=True)
    docseaurltxt = CharField(null=True)
    evtseacle = BigIntegerField(index=True)

    class Meta:
        db_table = 'docsea'


class Dpt(BaseModel):
    """
    département
    """
    dptart = CharField(null=True)
    dptcmt = CharField(null=True)
    dptcod = CharField()
    dptdatdeb = DateTimeField(null=True)
    dptdatfin = DateTimeField(null=True)
    dptlib = CharField()
    dptlibtri = CharField(null=True)
    dptlic = CharField(null=True)
    dptmodscrsen = CharField(null=True)
    dptnbrsen = BigIntegerField(null=True)
    dptnum = BigIntegerField(primary_key=True)
    dptnumtri = BigIntegerField()
    dptser = CharField()
    dptser2004 = CharField(null=True)
    dpturlcmp = CharField(null=True)
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    evetempub = CharField(null=True)
    regcod = CharField(index=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'dpt'


class Dptele(BaseModel):
    dptelecmt = CharField(null=True)
    dpteleid = BigIntegerField(primary_key=True)
    dptelenbrsie = BigIntegerField(null=True)
    dptelenbrsiepvr = BigIntegerField(null=True)
    dptnum = ForeignKeyField(db_column='dptnum', rel_model=Dpt, to_field='dptnum')
    eleid = BigIntegerField(index=True)
    participaidt1 = BigIntegerField(index=True, null=True)
    participaidt2 = BigIntegerField(index=True, null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    typelecod = CharField(index=True)
    valid2cod = CharField(index=True)
    validcod = CharField(index=True)

    class Meta:
        db_table = 'dptele'


class Ecr(BaseModel):
    autcod = CharField(index=True, null=True)
    docidt = BigIntegerField(null=True)
    ecrnum = BigIntegerField(primary_key=True)
    ecrnumtri = BigIntegerField()
    ecrqua = CharField(null=True)
    rapcod = BigIntegerField(index=True, null=True)
    signataire = CharField(null=True)
    texcod = BigIntegerField(index=True, null=True)
    typedoc = CharField(null=True)

    class Meta:
        db_table = 'ecr'


class Etadebman(BaseModel):
    """
     etadebmancod |            etadebmanlic
    --------------+-------------------------------------
     ELECTION     | Election
     REELECTION   | Réélection
     REMPLACE     | Remplace
     REN          | Renouvellement
     REN1         | Renouvellement 1
     REN2         | Renouvellement 2
     REN3         | Renouvellement 3
     REN4         | Renouvellement 4
     REN5         | Renouvellement 5
     REN6         | Renouvellement 6
     REN7         | Renouvellement 7
     REPRISE      | Reprise suite à fin fon. membre Gvt
    """
    etadebmancod = CharField(primary_key=True)
    etadebmanlib = CharField()
    etadebmanlibfem = CharField(null=True)
    etadebmanlibplu = CharField(null=True)
    etadebmanlic = CharField()
    etadebmanlicfem = CharField(null=True)
    etadebmanlicplu = CharField(null=True)
    etadebmanlil = CharField(null=True)
    etadebmanlilfem = CharField(null=True)
    etadebmanlilplu = CharField(null=True)
    etadebmannumtri = BigIntegerField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)

    class Meta:
        db_table = 'etadebman'


class Etafinman(BaseModel):
    """
     etafinmancod |                    etafinmanlic
    --------------+-----------------------------------------------------
     CESMEMGVT    | Membre Gouvernement
     CESDEPUTE    | Élu député
     CESMEMCC     | Nommé membre CC
     DEMPREMIN    | Démission (Premier ministre)
     ACTIF        | En Cours
     ANNCC        | Annulé par CC
     DECCC        | Dech. par CC
     DECEDE       | Décédé
     DEM          | Démissionnaire
     DEMMEMGVT    | Démission (Membre Gouvt)
     FINMAN       | Fin de mandat
     NONREELU     | Non réélu
     NONREP       | Ne se représente pas
     DEMDEPUTE    | Démission (Député)
     CESMANORD    | Cessation de mandat (1962)
     DEMMEMCC     | Démission (Membre CC)
     CESDEPUTEEUR | Élu député européen
     DEMDEPUTEEUR | Démission (Député européen)
     CESPREMIN    | Premier ministre
     REPEXE       | Reprise mandat d'ancien membre du Gvt
     CESMAN       | Cessation de mandat
     SEREP        | En cours, se représente
     DEMCC        | Démissionné d'office par le Conseil constitutionnel
    """
    etafinman = CharField()
    etafinmancod = CharField(primary_key=True)
    etafinmancodsirpas = CharField(null=True)
    etafinmanlibfem = CharField(null=True)
    etafinmanlibplu = CharField(null=True)
    etafinmanlic = CharField()
    etafinmanlicfem = CharField(null=True)
    etafinmanlicplu = CharField(null=True)
    etafinmanlil = CharField(null=True)
    etafinmanlilfem = CharField(null=True)
    etafinmanlilplu = CharField(null=True)
    etafinmannumtri = BigIntegerField(null=True)
    etafinmantemsirpas = CharField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)

    class Meta:
        db_table = 'etafinman'


class Etasen(BaseModel):
    """
     etasencod |         etasenlic
    -----------+----------------------------
     ACTIF     | En exercice
     ANCIEN    | Ancien sénateur
     ANCIEN4R  | Ancien sénateur 4e R.
     ANCIEN3R  | Ancien sénateur 3e R.
     ANCIENSC  | Ancien sénateur Communauté
     ANCIEN2E  | Ancien sénateur 2nd E.
    """
    etasencod = CharField(primary_key=True)
    etasenlib = CharField(null=True)
    etasenlibfem = CharField(null=True)
    etasenlibplu = CharField(null=True)
    etasenlic = CharField()
    etasenlicfem = CharField(null=True)
    etasenlicplu = CharField(null=True)
    etasenlil = CharField(null=True)
    etasenlilfem = CharField(null=True)
    etasenlilplu = CharField(null=True)
    etasennumtri = BigIntegerField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)

    class Meta:
        db_table = 'etasen'


class Grppol(BaseModel):
    """
    Groupe politique

     grppolcod |           grppolliccou
    -----------+-----------------------------------
     CRC       | Communiste républicain et citoyen
     NI        | NI
     RDSE      | RDSE
     RI        | RI
     RPR       | RPR
     SOC       | Socialiste et républicain
     UC        | UDI-UC
     AUCUN     | Aucun
     UMP       | Les Républicains
     C         | C
     CNIP      | C.N.I.P.
     CRARS     | CRARS
     FCD       | FCD
     GD        | G.D.
     GDSRG     | G.D.S.R.G.
     MRP       | MRP
     RDE       | R.D.E.
     RIAS      | R.I.A.S.
     RP        | RP
     RPCD      | RPCD
     UCDP      | U.C.D.P.
     UDR       | U.D.R.
     UNR       | U.N.R.
     UREI      | U.R.E.I.
     ECO       | Écologiste
    """
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    evetempub = CharField(null=True)
    grppolart = CharField(null=True)
    grppolcod = CharField(primary_key=True)
    grppolcodamelicou = CharField(null=True)
    grppolcodrepro = CharField(null=True)
    grppolcodscr = CharField(null=True)
    grppoldatcre = DateTimeField(null=True)
    grppoldatfin = DateTimeField(null=True)
    grppollibcou = CharField(null=True)
    grppolliccou = CharField(null=True)
    grppollilcou = CharField(null=True)
    grppolnumtri = BigIntegerField(null=True)
    grppolpre = CharField(null=True)
    grppolurlcmp = CharField(null=True)
    grppolurlsim = CharField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)
    typorgcod = ForeignKeyField(db_column='typorgcod', rel_model=TyporgSen, to_field='typorgcod')

    class Meta:
        db_table = 'grppol'


class QuaSen(BaseModel):
    """
     quacod |    qualic
    --------+--------------
     M.     | Monsieur
     Mme    | Madame
     Mlle   | Mademoiselle
    """
    quacod = CharField(primary_key=True)
    quacodsex = CharField(null=True)
    quacodsirpas = CharField(null=True)
    qualib = CharField(null=True)
    qualibplu = CharField(null=True)
    qualic = CharField()
    qualicplu = CharField(null=True)
    qualil = CharField(null=True)
    qualilplu = CharField(null=True)
    quanumtri = BigIntegerField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)

    class Meta:
        db_table = 'qua_sen'


class Sen(BaseModel):
    """
    Sénateur
    """
    catprocod2e = CharField(index=True, null=True)
    etasencod = ForeignKeyField(db_column='etasencod', rel_model=Etasen, to_field='etasencod')
    quacod = ForeignKeyField(db_column='quacod', rel_model=QuaSen, to_field='quacod')
    senburcommu = CharField(null=True)
    senburliccou = CharField(null=True)
    sencircou = CharField(null=True)
    sencircou3r = CharField(null=True)
    sencircou4r = CharField(null=True)
    sencirnumcou = ForeignKeyField(db_column='sencirnumcou', null=True, rel_model=Dpt, to_field='dptnum')
    sencirnumcou3r = BigIntegerField(null=True)
    sencirnumcou4r = BigIntegerField(null=True)
    sencomcodcou = ForeignKeyField(db_column='sencomcodcou', null=True, rel_model=Com, to_field='orgcod')
    sencomliccou = CharField(null=True)
    sencrinom = CharField(null=True)
    sendatderele = DateTimeField(index=True, null=True)
    sendatpreele = DateTimeField(null=True)
    sendespro2e = CharField(null=True)
    senfem = CharField(null=True)
    sengrppolcodcou = ForeignKeyField(db_column='sengrppolcodcou', null=True, rel_model=Grppol, to_field='grppolcod')
    sengrppolcodcou4r = CharField(index=True, null=True)
    sengrppolcommu = CharField(null=True)
    sengrppolliccou = CharField(null=True)
    senmat = CharField(primary_key=True)
    sennomdis = CharField(null=True)
    sennomdit = CharField(null=True)
    sennomuse = CharField()
    sennomusecap = CharField()
    senobs3r1 = CharField(null=True)
    senobs3r2 = CharField(null=True)
    senobs4r1 = CharField(null=True)
    senobs4r2 = CharField(null=True)
    senobscommu = CharField(null=True)
    senprenomuse = CharField()
    sentypappcou = CharField(null=True)
    sentypappcou4r = CharField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    titnobcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'sen'


class Elusen(BaseModel):
    """
    Mandat sénateur
    """
    dptnum = ForeignKeyField(db_column='dptnum', rel_model=Dpt, to_field='dptnum')
    eluanndeb = BigIntegerField(null=True)
    eluannfin = BigIntegerField(null=True)
    eludatcum = DateTimeField(null=True)
    eludatdeb = DateTimeField(index=True, null=True)
    eludatelu = DateTimeField(null=True)
    eludatfin = DateTimeField(index=True, null=True)
    eluid = BigIntegerField(primary_key=True)
    etadebmancod = ForeignKeyField(db_column='etadebmancod', rel_model=Etadebman, to_field='etadebmancod')
    etafinmancod = ForeignKeyField(db_column='etafinmancod', null=True, rel_model=Etafinman, to_field='etafinmancod')
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    senmat = ForeignKeyField(db_column='senmat', rel_model=Sen, to_field='senmat')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)
    turelucod = CharField(index=True)
    typmancod = CharField(index=True, null=True)

    class Meta:
        db_table = 'elusen'


class Etaloi(BaseModel):
    """
     etaloicod |              etaloilib
    -----------+--------------------------------------
     02        | fusionné
     05        | caduc
     04        | promulgué ou adopté (ppr)
     01        | en cours de discussion
     03        | rejeté
    """
    etaloicod = CharField(primary_key=True)
    etaloilib = CharField()

    class Meta:
        db_table = 'etaloi'


class Evtsea(BaseModel):
    """
    12 lignes dans cette table, 11 motion référendaire, 1 document produit en séance
    """
    evtseacle = BigIntegerField(primary_key=True)
    evtseadat = DateTimeField(null=True)
    lecassidt = CharField(index=True)
    loicod = CharField(index=True, null=True)
    typevtcod = CharField(index=True)

    class Meta:
        db_table = 'evtsea'


class Foncom(BaseModel):
    """
    Fonction dans commission

      foncomcod   |          foncomlic
    --------------+------------------------------
     MEMBRECOM    | Membre
     PDTCOM       | Président
     RAPGENCOM    | Rapporteur général
     SECRETCOM    | Secrétaire
     VICPDTCOM    | Vice-Président
     RAPCOM       | Rapporteur
     RAPADJCOM    | Rapporteur adjoint
     VICPDTHONCOM | Vice-Président d'honneur
     VICPDTPRECOM | Premier Vice-Président
     PDTRAPCOM    | Président et rapporteur
     VICPDTRAPCOM | Vice-Président et rapporteur
     SECRETRAPCOM | Secrétaire Rapporteur
    """
    foncomcod = CharField(primary_key=True)
    foncomlib = CharField()
    foncomlibfem = CharField(null=True)
    foncomlibfemplu = CharField(null=True)
    foncomlibplu = CharField(null=True)
    foncomlic = CharField()
    foncomlicfem = CharField(null=True)
    foncomlicfemplu = CharField(null=True)
    foncomlicplu = CharField(null=True)
    foncomlil = CharField(null=True)
    foncomlilfem = CharField(null=True)
    foncomlilfemplu = CharField(null=True)
    foncomlilplu = CharField(null=True)
    foncomnumtri = BigIntegerField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)

    class Meta:
        db_table = 'foncom'


class Fondelega(BaseModel):
    """
    Fonction dans délégation

      fondelcod   |                     fondellic
    --------------+---------------------------------------------------
     PDTDRTDEL    | Président de droit
     PDTEXECUTDEL | Président exécutif
     VICPDTDELDEL | Vice-Président délégué
     TRESORDEL    | Trésorier
     TRESORADJDEL | Trésorier adjoint
     DELEGUEDEL   | Membre
     DELSUPDEL    | Suppléant
     DELTITDEL    | Titulaire
     PDTDEL       | Président
     SECRETDEL    | Secrétaire
     VICPDTDEL    | Vice-Président
     SECRETGENDEL | Secrétaire Général
     AUTFONDEL    | Autre membre Bureau
     VICPDTPREDEL | Premier Vice-Président
     PDTDELDEL    | Président délégué
     SECRETADJDEL | Secrétaire adjoint
     CHEFDEL      | Chef
     VICPDTPRESIM | Premier Vice-Président, simplification des normes
     RAPGEN       | Rapporteur général
    """
    fondelcod = CharField(primary_key=True)
    fondellib = CharField()
    fondellibfem = CharField(null=True)
    fondellibfemplu = CharField(null=True)
    fondellibplu = CharField(null=True)
    fondellic = CharField()
    fondellicfem = CharField(null=True)
    fondellicfemplu = CharField(null=True)
    fondellicplu = CharField(null=True)
    fondellil = CharField(null=True)
    fondellilfem = CharField(null=True)
    fondellilfemplu = CharField(null=True)
    fondellilplu = CharField(null=True)
    fondelnumtri = BigIntegerField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)

    class Meta:
        db_table = 'fondelega'


class Fongrppol(BaseModel):
    """
    Fonction groupe politique

     fongrppolcod |      fongrppollic
    --------------+------------------------
     DELPOL       | Délégué
     MEMBREPOL    | Membre
     PDTPOL       | Président
     PDTDELPOL    | Président délégué
     VICPDTPOL    | Vice-Président
     VICPDTDELPOL | Vice-Président délégué
    """
    fongrppolcod = CharField(primary_key=True)
    fongrppollib = CharField()
    fongrppollibfem = CharField(null=True)
    fongrppollibfemplu = CharField(null=True)
    fongrppollibplu = CharField(null=True)
    fongrppollic = CharField()
    fongrppollicfem = CharField(null=True)
    fongrppollicfemplu = CharField(null=True)
    fongrppollicplu = CharField(null=True)
    fongrppollil = CharField(null=True)
    fongrppollilfem = CharField(null=True)
    fongrppollilfemplu = CharField(null=True)
    fongrppollilplu = CharField(null=True)
    fongrppolnumtri = BigIntegerField(null=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)

    class Meta:
        db_table = 'fongrppol'


class Memcom(BaseModel):
    """
    Membre commission
    """
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    evetempub = CharField(null=True)
    memcomdatdeb = DateTimeField(index=True, null=True)
    memcomdatfin = DateTimeField(index=True, null=True)
    memcomid = BigIntegerField(primary_key=True)
    memcomtitsup = CharField(null=True)
    orgcod = ForeignKeyField(db_column='orgcod', rel_model=Com, to_field='orgcod')
    senmat = ForeignKeyField(db_column='senmat', rel_model=Sen, to_field='senmat')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'memcom'


class Fonmemcom(BaseModel):
    """
    Fonction membre commission
    """
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    evetempub = CharField(null=True)
    foncomcod = ForeignKeyField(db_column='foncomcod', rel_model=Foncom, to_field='foncomcod')
    fonmemcomdatdeb = DateTimeField(index=True, null=True)
    fonmemcomdatfin = DateTimeField(index=True, null=True)
    fonmemcomid = BigIntegerField(primary_key=True)
    fonmemcomrngprt = BigIntegerField(null=True)
    memcomid = ForeignKeyField(db_column='memcomid', rel_model=Memcom, to_field='memcomid')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'fonmemcom'


class Memdelega(BaseModel):
    """
    Membre délégation
    """
    designcod = ForeignKeyField(db_column='designcod', rel_model=Designorg, to_field='designcod')
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    evetempub = CharField(null=True)
    memdelegadatdeb = DateTimeField(index=True, null=True)
    memdelegadatfin = DateTimeField(index=True, null=True)
    memdelegaid = BigIntegerField(primary_key=True)
    orgcod = ForeignKeyField(db_column='orgcod', rel_model=Delega, to_field='orgcod')
    senmat = ForeignKeyField(db_column='senmat', rel_model=Sen, to_field='senmat')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'memdelega'


class Fonmemdelega(BaseModel):
    """
    Fonction délégation
    """
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    evetempub = CharField(null=True)
    fondelcod = ForeignKeyField(db_column='fondelcod', rel_model=Fondelega, to_field='fondelcod')
    fonmemdeldatdeb = DateTimeField(index=True, null=True)
    fonmemdeldatfin = DateTimeField(index=True, null=True)
    fonmemdelid = BigIntegerField(primary_key=True)
    fonmemdelrngele = BigIntegerField(null=True)
    memdelegaid = ForeignKeyField(db_column='memdelegaid', rel_model=Memdelega, to_field='memdelegaid')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'fonmemdelega'


class Typapppol(BaseModel):
    """
    Type de lien entre sénateur et groupe politique
     typapppolcod | typapppollib
    --------------+--------------
     N            | Membre
     R            | Rattaché
     A            | Apparenté
    """
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    typapppolcod = CharField(primary_key=True)
    typapppollib = CharField(null=True)
    typapppollibfem = CharField(null=True)
    typapppollibplu = CharField(null=True)
    typapppollic = CharField(null=True)
    typapppollicfem = CharField(null=True)
    typapppollicplu = CharField(null=True)
    typapppollil = CharField(null=True)
    typapppollilfem = CharField(null=True)
    typapppollilplu = CharField(null=True)
    typapppolnumtri = BigIntegerField(null=True)

    class Meta:
        db_table = 'typapppol'


class Memgrppol(BaseModel):
    """
    Liason entre sénateur et groupe politique
    """
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    evetempub = CharField(null=True)
    grppolcod = ForeignKeyField(db_column='grppolcod', rel_model=Grppol, to_field='grppolcod')
    memgrppoldatdeb = DateTimeField(index=True, null=True)
    memgrppoldatfin = DateTimeField(index=True, null=True)
    memgrppolid = BigIntegerField(primary_key=True)
    senmat = ForeignKeyField(db_column='senmat', rel_model=Sen, to_field='senmat')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)
    typapppolcod = ForeignKeyField(db_column='typapppolcod', rel_model=Typapppol, to_field='typapppolcod')

    class Meta:
        db_table = 'memgrppol'


class Fonmemgrppol(BaseModel):
    """
    Fonction sénateur dans groupe poligique
    """
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    evetempub = CharField(null=True)
    fongrppolcod = ForeignKeyField(db_column='fongrppolcod', rel_model=Fongrppol, to_field='fongrppolcod')
    fonmemgrppoldatdeb = DateTimeField(index=True, null=True)
    fonmemgrppoldatfin = DateTimeField(index=True, null=True)
    fonmemgrppolid = BigIntegerField(primary_key=True)
    memgrppolid = ForeignKeyField(db_column='memgrppolid', rel_model=Memgrppol, to_field='memgrppolid')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'fonmemgrppol'


class Forpub(BaseModel):
    """
     forpubcod |   forpublib
    -----------+---------------
     NOR       | Normal
     SOM       | Sommaire seul
    """
    forpubcod = CharField(primary_key=True)
    forpublib = CharField()

    class Meta:
        db_table = 'forpub'


class Gen(BaseModel):
    """
     gencod |      genlib
    --------+------------------
     M      | Masculin
     F      | Féminin
     P      | Pluriel masculin
     Q      | Pluriel féminin
    """
    gencod = CharField()
    genlib = CharField()

    class Meta:
        db_table = 'gen'


class Lecass(BaseModel):
    """
    ?
    """
    aliasppr = CharField(null=True)
    codass = CharField()
    debatsurl = CharField(null=True)
    depot_only = CharField()
    lecassame = CharField(null=True)
    lecassamecom = CharField(null=True)
    lecassamecomdat = DateTimeField(null=True)
    lecassamedat = DateTimeField(null=True)
    lecassameses = IntegerField(null=True)
    lecassamesescom = IntegerField(null=True)
    lecassidt = CharField(primary_key=True)
    lecidt = CharField(index=True)
    libppr = CharField(null=True)
    loiintmod = CharField(null=True)
    ordreass = BigIntegerField()
    orgcod = CharField(index=True, null=True)
    orippr = CharField(null=True)
    ptlnot = CharField(null=True)
    ptlnot2 = CharField(null=True)
    ptlnot3 = CharField(null=True)
    ptlnum = IntegerField(null=True)
    ptlnumcom = IntegerField(null=True)
    ptlnumcpl = CharField(null=True)
    ptlnumcpl2 = CharField(null=True)
    ptlnumcpl3 = CharField(null=True)
    ptlurl = CharField(null=True)
    ptlurl2 = CharField(null=True)
    ptlurl3 = CharField(null=True)
    ptlurlcom = CharField(null=True)
    reucom = CharField(null=True)
    sesann = BigIntegerField(null=True)
    sesppr = BigIntegerField(null=True)

    class Meta:
        db_table = 'lecass'


class Lecassrap(BaseModel):
    lecassidt = CharField(index=True)
    lecassrapord = BigIntegerField(null=True)
    rapcod = BigIntegerField(index=True)

    class Meta:
        db_table = 'lecassrap'
        indexes = (
            (('lecassidt', 'rapcod'), True),
        )
        primary_key = CompositeKey('lecassidt', 'rapcod')


class Libcom(BaseModel):
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    libcomart = CharField(null=True)
    libcomdatdeb = DateTimeField(index=True)
    libcomdatfin = DateTimeField(index=True, null=True)
    libcomid = BigIntegerField(primary_key=True)
    libcomlibameli = CharField(null=True)
    libcomlilmin = CharField(null=True)
    orgcod = ForeignKeyField(db_column='orgcod', rel_model=Com, to_field='orgcod')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'libcom'
        indexes = (
            (('orgcod', 'libcomdatdeb'), True),
        )


class Libdelega(BaseModel):
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    libdelegaart = CharField(null=True)
    libdelegadatdeb = DateTimeField(index=True)
    libdelegadatfin = DateTimeField(index=True, null=True)
    libdelegaid = BigIntegerField(primary_key=True)
    orgcod = ForeignKeyField(db_column='orgcod', rel_model=Delega, to_field='orgcod')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'libdelega'
        indexes = (
            (('orgcod', 'libdelegadatdeb'), True),
        )


class Libgrppol(BaseModel):
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    grppolcod = ForeignKeyField(db_column='grppolcod', rel_model=Grppol, to_field='grppolcod')
    libgrppolart = CharField(null=True)
    libgrppolcodameli = CharField(null=True)
    libgrppoldatdeb = DateTimeField(index=True)
    libgrppoldatfin = DateTimeField(index=True, null=True)
    libgrppolid = BigIntegerField(primary_key=True)
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'libgrppol'
        indexes = (
            (('grppolcod', 'libgrppoldatdeb'), True),
        )


class Rap(BaseModel):
    """
    Rapport
    """
    blecod = CharField(null=True)
    coddenrap = CharField()
    date_depot = DateTimeField()
    depot_only = CharField(null=True)
    forpubcod = CharField(null=True)
    numerobis = CharField(null=True)
    prix = CharField(null=True)
    rapann = IntegerField(null=True)
    rapcod = BigIntegerField(primary_key=True)
    rapdatsea = DateTimeField(null=True)
    rapfac = IntegerField(null=True)
    rapnum = BigIntegerField(index=True, null=True)
    rapnuman = BigIntegerField(null=True)
    rapres = CharField(null=True)
    rapsoustit = CharField(null=True)
    raptil = CharField(null=True)
    raptitcou = CharField(null=True)
    raptom = IntegerField(null=True)
    rapurl = CharField(null=True)
    rapvol = IntegerField(null=True)
    sesann = BigIntegerField()
    typurl = CharField()
    url2 = CharField(null=True)
    url2txt = CharField(null=True)
    url3 = CharField(null=True)
    url3txt = CharField(null=True)
    url4 = CharField(null=True)
    url4txt = CharField(null=True)

    class Meta:
        db_table = 'rap'


class Lnkrap(BaseModel):
    """
    Lien entre rapports : pour les mises à jour (rare)
    Cette table ne contient que 19 lignes
    """
    rapcodenf = ForeignKeyField(db_column='rapcodenf', rel_model=Rap, to_field='rapcod')
    rapcodper = ForeignKeyField(db_column='rapcodper', rel_model=Rap, related_name='rap_rapcodper_set', to_field='rapcod')
    rapenfdsc = CharField(null=True)
    rapperdsc = CharField(null=True)

    class Meta:
        db_table = 'lnkrap'
        indexes = (
            (('rapcodper', 'rapcodenf'), True),
        )
        primary_key = CompositeKey('rapcodenf', 'rapcodper')


class Loi(BaseModel):
    date_decision = DateTimeField(null=True)
    date_loi = DateTimeField(null=True)
    deccoccod = CharField(null=True)
    deccocurl = CharField(null=True)
    doscocurl = CharField(null=True)
    etaloicod = CharField(null=True)
    loicod = CharField(primary_key=True)
    loicodmai = CharField(null=True)
    loidatjo = DateTimeField(null=True)
    loidatjo2 = DateTimeField(null=True)
    loidatjo3 = DateTimeField(null=True)
    loient = CharField(null=True)
    loiint = CharField(null=True)
    loiintori = CharField(null=True)
    loinoudelibcod = CharField(null=True)
    loinumjo = CharField(null=True)
    loinumjo2 = CharField(null=True)
    loinumjo3 = CharField(null=True)
    loitit = CharField(null=True)
    loititjo = CharField(null=True)
    motclef = CharField(null=True)
    motionloiorigcod = CharField(index=True, null=True)
    num_decision = CharField(null=True)
    numero = CharField(null=True)
    objet = TextField(null=True)
    orgcod = CharField(null=True)
    proaccdat = DateTimeField(null=True)
    proaccoppdat = DateTimeField(null=True)
    retproaccdat = DateTimeField(null=True)
    saisine_date = DateTimeField(null=True)
    saisine_par = CharField(null=True)
    signet = CharField(null=True)
    signetalt = CharField(null=True)
    typloicod = CharField()
    urgence = CharField(null=True)
    url_an = CharField(null=True)
    url_jo = CharField(null=True)
    url_jo2 = CharField(null=True)
    url_jo3 = CharField(null=True)
    url_ordonnance = CharField(null=True)
    url_presart = CharField(null=True)

    class Meta:
        db_table = 'loi'


class The(BaseModel):
    """
    Thème

     thecle |               thelib               |                     theali
    --------+------------------------------------+------------------------------------------------
          1 | Collectivités territoriales        | aux collectivités territoriales
          2 | Agriculture et pêche               | à l'agriculture et à la pêche
          3 | Société                            | à la société
          4 | Affaires étrangères et coopération | aux affaires étrangères et à la coopération
          5 | Police et sécurité                 | à la police et à la sécurité
          7 | Environnement                      | à l'environnement
          8 | Union européenne                   | à l'Union Européenne
          9 | Pouvoirs publics et Constitution   | aux pouvoirs publics et à la Constitution
         10 | Budget                             | au budget
         11 | Traités et conventions             | aux traités et aux conventions
         12 | Culture                            | à la culture
         13 | Famille                            | à la famille
         14 | Justice                            | à la justice
         15 | Recherche, sciences et techniques  | à la recherche, aux sciences et aux techniques
         16 | Logement et urbanisme              | au logement et à l'urbanisme
         17 | Économie et finances, fiscalité    | à l'économie, aux finances et à la fiscalité
         18 | Outre-mer                          | à l'outre-mer
         19 | Fonction publique                  | à la fonction publique
         20 | Questions sociales et santé        | aux questions sociales et à la santé
         21 | Transports                         | aux transports
         22 | Travail                            | au travail
         23 | Anciens combattants                | aux anciens combattants
         24 | Éducation                          | à l'éducation
         25 | Sécurité sociale                   | à la Sécurité sociale
         28 | PME, commerce et artisanat         | aux PME, au commerce et à l'artisanat
         29 | Défense                            | à la défense
         30 | Aménagement du territoire          | à l'aménagement du territoire
         31 | Sports                             | aux sports
         32 | Énergie                            | à l'énergie
         33 | Entreprises                        | aux entreprises
    """
    theali = CharField(null=True)
    thecle = PrimaryKeyField()
    thelib = CharField()

    class Meta:
        db_table = 'the'


class Loithe(BaseModel):
    loicod = ForeignKeyField(db_column='loicod', rel_model=Loi, to_field='loicod')
    thecle = ForeignKeyField(db_column='thecle', rel_model=The, to_field='thecle')

    class Meta:
        db_table = 'loithe'
        indexes = (
            (('loicod', 'thecle'), True),
        )
        primary_key = CompositeKey('loicod', 'thecle')


class Natloi(BaseModel):
    """
    Nature loi

                    groupe                |                natloilib
    --------------------------------------+------------------------------------------
     pjl                                  | projet de loi
     ppl                                  | proposition de loi
     ppr                                  | proposition de risolution
     cvn                                  | convention
    """
    groupe = CharField(primary_key=True)
    natloilib = CharField()

    class Meta:
        db_table = 'natloi'


class Org(BaseModel):
    """
    Organisation : commission, groupe de travail, mission, délégation
    """
    codass = CharField(null=True)
    html_color = CharField(null=True)
    inttra = CharField(null=True)
    org_de = CharField(null=True)
    orgcod = CharField(primary_key=True)
    orgdatdeb = DateTimeField(null=True)
    orgdatdebcop = DateTimeField(null=True)
    orgdatfin = DateTimeField(null=True)
    orgdatfincop = DateTimeField(null=True)
    orglibaff = CharField(null=True)
    orglibcou = CharField(null=True)
    orgliblon = CharField(null=True)
    orgnom = CharField()
    orgnomcouv = CharField(null=True)
    orgord = IntegerField(null=True)
    orgurl = CharField(null=True)
    senorgcod = CharField(null=True)
    typorgcod = CharField(index=True)
    urltra = CharField(null=True)

    class Meta:
        db_table = 'org'


class Orgnomhis(BaseModel):
    intra = CharField(null=True)
    onhfin = DateTimeField()
    onhnum = BigIntegerField(primary_key=True)
    org_de = CharField()
    orgcod = ForeignKeyField(db_column='orgcod', rel_model=Org, to_field='orgcod')
    orglibcou = CharField()
    orgliblon = CharField()
    orgnom = CharField()
    orgnomcouv = CharField(null=True)

    class Meta:
        db_table = 'orgnomhis'


class Orippr(BaseModel):
    """
    S         | Sénateur
    C         | Saisine par commission
    E         | Commission des Affaires européennes
    """
    oripprcod = CharField(primary_key=True)
    oripprlib = CharField()

    class Meta:
        db_table = 'orippr'


class Oritxt(BaseModel):
    """
    Origine du texte

     oritxtcod | oritxtlib
    -----------+---------------------------------------------------------------------------------------------------------------
     26        | considéré comme modifié par l'Assemblée nationale en application de l'article 49, alinéa 3, de la Constitution
     29        | de la commission
     0         | transmis au Sénat
     4         | déposé à l'Assemblée Nationale
     2         | adopté avec modifications par le Sénat
     5         | adopté par l'Assemblée nationale
     7         | modifié par le Sénat
     9         | adopté définitivement par le Sénat
     11        | adopté par le Sénat
     12        | déclaré irrecevable
     13        | renvoyé en commission
     15        | retiré par son auteur
     17        | considéré comme adopté par l'Assemblée nationale en application de l'article 49, alinéa 3, de la Constitution
     1         | déposé au Sénat
     25        | rejeté par la commission
     30        | de la commission (AN)
     27        | rejeté par l'adoption d'une question préalable
     28        | non modifié par la commission qui propose l'adoption d'une question préalable
     32        | déclaré irrecevable par le Gouvernement
     33        | considéré comme adopté par la commission
     34        | devenu résolution du Sénat
     35        | transmis à la commission
     31        | rejeté par l'adoption d'une exception d'irrecevabilité
     36        | résultat des travaux de la commission
     3         | transmis à l'Assemblée nationale
     6         | adopté sans modification par le Sénat
     8         | rejeté par le Sénat
     10        | retiré de l'ordre du jour
     14        | adopté définitivement par l'Assemblée nationale
     16        | adopté par le Congrès
     18        | adopté avec modifications par l'Assemblée nationale
     19        | adopté sans modification par l'Assemblée nationale
     20        | rejeté par l'Assemblée nationale
     21        | rejeté par suite de l'adoption des conclusions négatives de la commission
     22        | modifié par l'Assemblée nationale
     23        | adopté par la commission
     24        | retiré par le Premier ministre
    """
    codass = CharField(null=True)
    oriordre = CharField(null=True)
    oritxtado = CharField(null=True)
    oritxtcod = CharField(primary_key=True)
    oritxtlib = CharField()
    oritxtlibfem = CharField()
    oritxtmod = CharField(null=True)
    oritxtorg = CharField(null=True)

    class Meta:
        db_table = 'oritxt'


class Posvot(BaseModel):
    """
    Position vote

     posvotcod | posvotlib
    -----------+------------
     1         | pour
     2         | contre
     3         | abstention
     4         | non-votant
    """
    posvotcod = CharField(primary_key=True)
    posvotlib = CharField()

    class Meta:
        db_table = 'posvot'


class Qua(BaseModel):
    """
     quacod |    qualic    |    quaabr    |  quaabrplu
    --------+--------------+--------------+--------------
     2      | Madame       | Mme          | Mmes
     1      | Monsieur     | M.           | MM.
     3      | Mademoiselle | Mlle         | Mlles
     4      | Aucun        |              |
    """
    quaabr = CharField()
    quaabrplu = CharField()
    quacod = CharField(primary_key=True)
    qualic = CharField()

    class Meta:
        db_table = 'qua'


class Raporg(BaseModel):
    orgcod = ForeignKeyField(db_column='orgcod', rel_model=Org, related_name='org_orgcod_set', to_field='orgcod')
    rapcod = ForeignKeyField(db_column='rapcod', rel_model=Rap, to_field='rapcod')

    class Meta:
        db_table = 'raporg'
        indexes = (
            (('rapcod', 'orgcod'), True),
        )
        primary_key = CompositeKey('orgcod', 'rapcod')


class Rapthe(BaseModel):
    rapcod = ForeignKeyField(db_column='rapcod', rel_model=Rap, to_field='rapcod')
    thecle = ForeignKeyField(db_column='thecle', rel_model=The, to_field='thecle')

    class Meta:
        db_table = 'rapthe'
        indexes = (
            (('rapcod', 'thecle'), True),
        )
        primary_key = CompositeKey('rapcod', 'thecle')


class Rolsig(BaseModel):
    """
     signataire |    rolsiglib
    ------------+------------------
     o          | primo-signataire
     n          | coauteur
     p          | président
    """
    rolsiglib = CharField()
    signataire = CharField(primary_key=True)

    class Meta:
        db_table = 'rolsig'


class Scr(BaseModel):
    """
    Scrutin
    """
    code = BigIntegerField(index=True, null=True)
    scrcon = BigIntegerField(null=True)
    scrconsea = BigIntegerField(null=True)
    scrdat = DateTimeField(null=True)
    scrint = CharField(null=True)
    scrmaj = BigIntegerField(null=True)
    scrmajsea = BigIntegerField(null=True)
    scrnum = BigIntegerField()
    scrpou = BigIntegerField(null=True)
    scrpousea = BigIntegerField(null=True)
    scrsuf = BigIntegerField(null=True)
    scrsufsea = BigIntegerField(null=True)
    scrvot = BigIntegerField(null=True)
    scrvotsea = BigIntegerField(null=True)
    sesann = BigIntegerField(index=True)

    class Meta:
        db_table = 'scr'
        indexes = (
            (('sesann', 'scrnum'), True),
        )
        primary_key = CompositeKey('scrnum', 'sesann')


class Senbur(BaseModel):
    """
    Membre du bureau
    """
    burcod = ForeignKeyField(db_column='burcod', rel_model=Bur, to_field='burcod')
    evelib = CharField(null=True)
    evelic = CharField(null=True)
    evelil = CharField(null=True)
    eveobs = CharField(null=True)
    evetempub = CharField(null=True)
    senburdatdeb = DateTimeField(index=True, null=True)
    senburdatfin = DateTimeField(index=True, null=True)
    senburhon = CharField(null=True)
    senburid = BigIntegerField(primary_key=True)
    senburrelint = CharField(null=True)
    senburrngele = BigIntegerField(null=True)
    senmat = ForeignKeyField(db_column='senmat', rel_model=Sen, to_field='senmat')
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)
    temvalcod = CharField(index=True, null=True)

    class Meta:
        db_table = 'senbur'


class Sennom(BaseModel):
    """
    Nomination sénateur ?
    """
    quacod = ForeignKeyField(db_column='quacod', rel_model=QuaSen, to_field='quacod')
    senmat = ForeignKeyField(db_column='senmat', rel_model=Sen, to_field='senmat')
    sennomdatdeb = DateTimeField(index=True)
    sennomdatfin = DateTimeField(index=True, null=True)
    sennomid = BigIntegerField(primary_key=True)
    sennomtec = CharField()
    sennomuse = CharField()
    sennomusecap = CharField()
    senprenomuse = CharField()
    syscredat = DateTimeField(null=True)
    sysmajdat = DateTimeField(null=True)

    class Meta:
        db_table = 'sennom'
        indexes = (
            (('senmat', 'sennomdatdeb'), True),
        )


class Stavot(BaseModel):
    """
     stavotidt |                  stavotlib
    -----------+----------------------------------------------
     0         | Sans statut
     1         | Position de vote systématiquement pour
     2         | Position de vote systématiquement contre
     3         | Position de vote systématiquement abstention
     4         | Position de vote systématique
     5         | Congé
     6         | Excusé
     7         | Membre de la Haute Cour
     8         | Président de séance
     9         | Membre du gouvernement
     10        | Député
     11        | Député européen
    """
    stavotidt = CharField(primary_key=True)
    stavotlib = CharField()

    class Meta:
        db_table = 'stavot'


class Texte(BaseModel):
    datrejet_disc_immediate = DateTimeField(null=True)
    lecassidt = CharField(index=True)
    numerobis = CharField(null=True)
    orgcod = CharField(null=True)
    oritxtcod = CharField(index=True, null=True)
    prix = CharField(null=True)
    reserve_comspe = CharField(null=True)
    sesann = BigIntegerField(null=True)
    texace = CharField(null=True)
    texcod = BigIntegerField(primary_key=True)
    texdatsea = DateTimeField(null=True)
    texnum = BigIntegerField(index=True, null=True)
    texurl = CharField(null=True)
    txtoritxtdat = DateTimeField()
    typtxtcod = CharField()
    typurl = CharField(index=True)
    url2 = CharField(null=True)
    url2txt = CharField(null=True)
    url3 = CharField(null=True)
    url3txt = CharField(null=True)
    url4 = CharField(null=True)
    url4txt = CharField(null=True)

    class Meta:
        db_table = 'texte'


class TexteAncien(BaseModel):
    article_type = CharField(null=True)
    date_effet = DateTimeField(null=True)
    fichier = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    lecture = CharField(null=True)
    libelle = CharField(null=True)
    numero = BigIntegerField()
    origine = CharField()
    rectifie = BigIntegerField()
    sesann = BigIntegerField()
    statut = CharField(null=True)
    type_texte = CharField(null=True)
    urgence = BigIntegerField()

    class Meta:
        db_table = 'texte_ancien'


class Titsen(BaseModel):
    """
     titsencod |   titsenlib
    -----------+----------------
     0         | Sénateur
     1         | Président
     2         | Vice-Président
    """
    titsencod = CharField(primary_key=True)
    titsenlib = CharField(null=True)

    class Meta:
        db_table = 'titsen'


class Typatt(BaseModel):
    """
     typattcod |      typattlib
    -----------+----------------------
     S         | Synthèse (4 pages)
     C         | Communiqué de presse
    """
    typattcod = CharField(primary_key=True)
    typattlib = CharField()

    class Meta:
        db_table = 'typatt'


class Typaut(BaseModel):
    """
     typautcod |              typautlib
    -----------+--------------------------------------
     1         | sénateur
     2         | collectif
     3         | député
     4         | ministre
     5         | groupe politique
     6         | divers
    """
    typautcod = CharField(primary_key=True)
    typautlib = CharField()

    class Meta:
        db_table = 'typaut'


class Typevtsea(BaseModel):
    """
     typevtcod |         typevtlib
    -----------+----------------------------
     DOC       | Document produit en séance
     MOR       | Motion référendaire
    """
    typevtcod = CharField(primary_key=True)
    typevtlib = CharField()

    class Meta:
        db_table = 'typevtsea'


class Typlec(BaseModel):
    """
     typleccod |                          typleclib                           | typlecord
    -----------+--------------------------------------------------------------+-----------
     2         | Deuxième lecture                                             |         2
     1         | Première lecture                                             |         1
     3         | Troisième lecture                                            |         3
     4         | Commission mixte paritaire                                   |       100
     5         | Nouvelle lecture                                             |       200
     7         | Quatrième lecture                                            |         4
     6         | Lecture définitive                                           |       300
     8         | Congrès du Parlement                                         |       400
     9         | Référendum                                                   |       500
    """
    typleccod = CharField(primary_key=True)
    typleclib = CharField()
    typlecord = BigIntegerField(null=True)

    class Meta:
        db_table = 'typlec'


class Typloi(BaseModel):
    """
     typloicod |                groupe                |                                    typloilib
    -----------+--------------------------------------+----------------------------------------------------------------------------------
     ppro      | ppl                                  | proposition de loi de programmation
     pplc      | ppl                                  | proposition de loi constitutionnelle
     pjlr      | pjl                                  | projet de loi de finances rectificative
     pjlg      | pjl                                  | projet de loi de règlement
     pjl       | pjl                                  | projet de loi
     pjlf      | pjl                                  | projet de loi de finances
     ppl       | ppl                                  | proposition de loi
     mref      |                                      | motion référendaire
     pjfs      | pjl                                  | projet de loi de financement sécurité sociale
     pjlo      | pjl                                  | projet de loi organique
     pjlc      | pjl                                  | projet de loi constitutionnelle
     pplo      | ppl                                  | proposition de loi organique
     cvn       | cvn                                  | convention
     pac       | ppr                                  | résolution européenne
     ppre      | ppr                                  | modification réglement Sénat
     enq       | ppr                                  | commission d'enquête
     ppra      | ppr                                  | proposition de résolution autre
     pprp      | ppr                                  | résolution en application de l'article 34-1
     refe      | ppl                                  | proposition de loi référendaire
     prog      | pjl                                  | projet de loi de programmation
     orie      | pjl                                  | Projet de loi d'orientation
     cadr      | pjl                                  | projet de loi cadre
     pfsr      | pjl                                  | projet de loi de financement rectificative de la sécurité sociale
    """
    groupe = CharField(null=True)
    typloicod = CharField(primary_key=True)
    typloide = CharField(null=True)
    typloiden = CharField(null=True)
    typloidenplu = CharField(null=True)
    typloigen = CharField(null=True)
    typloilib = CharField()
    typloitit = CharField(null=True)

    class Meta:
        db_table = 'typloi'


class Typorg(BaseModel):
    """
     typorgcod |                          typorglib                           |          typorgurl           |        typorgtitens
    -----------+--------------------------------------------------------------+------------------------------+-----------------------------
     GRTRA     | Groupe de travail                                            | /commission/                 | groupes de travail
     COM       | commission permanente                                        | /commission/                 | commissions
     COENQ     | commission d'enquête                                         | /commission/                 | commissions
     GRPAM     | groupe interparlementaire d'amitié                           | /international/gs_pres.html  | groupes interparlementaires
     OFFPA     | office parlementaire                                         | /opecst/                     | offices
     DELEG     | délégation                                                   | /offices_deleg_observatoire/ | délégations
     MISS      | mission d'information                                        | /commission/missions/        | missions d'information
     PRES      | présidence                                                   | /presidence/                 | présidence
     OBSER     | observatoire                                                 | /offices_deleg_observatoire/ | l'observatoire
     GRETU     | groupe d'étude                                               | /grpetu/etulst.html          | groupes d'étude
     CONTR     | mission de contrôle                                          | /controle/                   | contrôle
     COSPE     | commission spéciale                                          | /commission/spec/            | commissions spéciales
     OPARL     | organisme parlementaire                                      |                              | organismes parlementaires
    """
    typorgcod = CharField(primary_key=True)
    typorglib = CharField()
    typorgtitens = CharField(null=True)
    typorgurl = CharField(null=True)

    class Meta:
        db_table = 'typorg'


class Typrap(BaseModel):
    """
     typraprap |                          typraplib
    -----------+--------------------------------------------------------------
     COLTE     | Etude du service de Collectivités Territoriale
     ACTSE     | Rapport d'activité du Sénat
     LEGIS     | Rapport Législatif
     INFOR     | Rapport d'information
     OFFPA     | Rapport d'office parlementaire
     ENQUE     | Rapport de commission d'enquête
     LCOMP     | Etude de législation comparée
     APLEG     | Rapport d'application des lois
     AMITI     | Rapport de groupe interparlementaire d'amitié
     ACTCO     | Actes de colloque
     POUPU     | Recueil des textes sur les pouvoirs publics
     ETJUR     | Rapport du service des Etudes Juridiques
     REFIN     | Rapport sur l'institution sénatoriale
     DIVET     | Document d'étude
     REGSE     | Réglement du Sénat
     APLOI     | Rapport sur l'application des lois
     ETECO     | Etude écononique
    """
    catrapcod = CharField(null=True)
    typrapind = CharField()
    typraplib = CharField()
    typraplibplu = CharField(null=True)
    typrapnot = CharField(null=True)
    typraprap = CharField(primary_key=True)
    typraprep = CharField(null=True)
    typrapses = CharField(null=True)
    typrapurl = CharField(null=True)

    class Meta:
        db_table = 'typrap'


class Typtxt(BaseModel):
    """
     typtxtcod |              typtxtlib
    -----------+--------------------------------------
     1         | texte de loi
     2         | question préalable
     3         | recours
     4         | lettre rectificative
    """
    typtxtcod = CharField(primary_key=True)
    typtxtlib = CharField()

    class Meta:
        db_table = 'typtxt'


class Typurl(BaseModel):
    """
     typurl |                libtypurl
    --------+------------------------------------------
     I      | Interne
     E      | Externe
     0      | Pas d'URL
     S      | Sous embargo
    """
    libtypurl = CharField()
    typurl = CharField(primary_key=True)

    class Meta:
        db_table = 'typurl'


class Votsen(BaseModel):
    """
    Vote par sénateur
    """
    posvotcod = CharField(index=True, null=True)
    scrnum = BigIntegerField()
    senmat = CharField()
    senmatdel = CharField(null=True)
    sesann = BigIntegerField()
    stavotidt = CharField(index=True)
    titsencod = CharField(index=True)

    class Meta:
        db_table = 'votsen'
        indexes = (
            (('sesann', 'scrnum'), False),
            (('sesann', 'scrnum', 'senmat'), True),
        )
        primary_key = CompositeKey('scrnum', 'senmat', 'sesann')


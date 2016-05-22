# -*- coding: utf-8 -*-

from peewee import *

database = PostgresqlDatabase('ameli', **{})


class UnknownField(object):
    pass


class BaseModel(Model):
    class Meta:
        database = database


class Avicom(BaseModel):
    """
     id |        lib         | cod
    ----+--------------------+-----
     F  | Favorable          | F
     D  | Défavorable        | D
     S  | Sagesse du Sénat   | S
     N  | Néant              |
     R  | Demande de retrait | R
    """
    cod = CharField()
    id = CharField(primary_key=True)
    lib = CharField()

    class Meta:
        db_table = 'avicom'


class Avigvt(BaseModel):
    """
     id |        lib         | cod
    ----+--------------------+-----
     F  | Favorable          | F
     D  | Défavorable        | D
     S  | Sagesse du Sénat   | S
     N  | Néant              |
     R  | Demande de retrait | R
    """
    cod = CharField()
    id = CharField(primary_key=True)
    lib = CharField()

    class Meta:
        db_table = 'avigvt'


class Discom(BaseModel):

    class Meta:
        db_table = 'discom'


class Ent(BaseModel):
    act = CharField(null=True)
    typ = CharField()

    class Meta:
        db_table = 'ent'


class Ideamd(BaseModel):

    class Meta:
        db_table = 'ideamd'


class Irr(BaseModel):
    """
                          lib                      | cod
    -----------------------------------------------+------
     art 40 de la Constitution                     | 40
     LOLF                                          | ORG
     article 41 de la Constitution                 | 41
     article 44, alinéa 2 de la Constitution       | 44
     art. L.O 111-3 du code de la sécurité sociale | 45
     art 48, alinéa 3 du Règlement du Sénat        | 48
     art 48, alinéas 5 et 6 du Règlement du Sénat  | 42
     autre irrecevabilité                          | AUT
     LOLF (non diffusée)                           | ORG2
    """
    art = CharField(null=True)
    cod = CharField()
    lib = CharField()
    libirr = CharField(null=True)
    lilmin = CharField(null=True)

    class Meta:
        db_table = 'irr'


class Mot(BaseModel):
    """
                lib             |   cod
    ----------------------------+----------
     Exception d'irrecevabilité | EI
     Question préalable         | QP
     Renvoi en commission       | Rcom
     Motion préjudicielle       | M. Prej
     Motion incidente           | M. Incid
    """
    cod = CharField(null=True)
    int = CharField(null=True)
    lib = CharField()
    libnbe = CharField(null=True)
    ord = BigIntegerField()

    class Meta:
        db_table = 'mot'


class Sor(BaseModel):
    """
     id |           lib            | cod | typ
    ----+--------------------------+-----+-----
     A  | Adopté                   | A   | S
     R  | Retiré                   | R   | S
     J  | Rejeté                   | RJS | S
     K  | Rejeté - vote unique     | RJB | S
     N  | Non soutenu              | N   | S
     S  | Tombé                    | S   | S
     B  | Adopté - vote unique     | AB  | S
     1  | Adopté                   | A   | C
     2  | Adopté avec modification | AM  | C
     3  | Rejeté                   | RJ  | C
     4  | Retiré                   | RET | C
     5  | Satisfait ou sans objet  | SO  | C
     6  |                          | NE  | C
    """
    cod = CharField()
    id = CharField(primary_key=True)
    lib = CharField()
    typ = CharField()

    class Meta:
        db_table = 'sor'


class Etatxt(BaseModel):
    """
     id |         lic         |                     lib                     | txttyp
    ----+---------------------+---------------------------------------------+--------
     10 | Adoption            | Le Sénat a adopté                           | S
     11 | Adoption définitive | Le Sénat a adopté définitivement            | S
     12 | Rejet               | Le Sénat n'a pas adopté                     | S
      0 |                     |                                             | A
     20 | Adoption            | Le texte est adopté par la commission       | C
     25 | Rejet               | Le texte n'est pas adopté par la commission | C
    """
    id = BigIntegerField(primary_key=True)
    lib = CharField()
    lic = CharField()
    txttyp = CharField()

    class Meta:
        db_table = 'etatxt'


class Typses(BaseModel):
    """
     id |               lib
    ----+----------------------------------
      1 | Session Ordinaire
      2 | Session extraordinaire
      3 | Seconde session extraordinaire
      4 | Troisième session extraordinaire
    """
    lib = CharField(null=True)

    class Meta:
        db_table = 'typses'


class Ses(BaseModel):
    """
    id | typid | ann  |                      lil
    ----+-------+------+-----------------------------------------------
     26 |     2 | 2010 | Première session extraordinaire de 2010-2011
     35 |     1 | 2013 | 2013-2014
     27 |     3 | 2010 | Deuxième session extraordinaire 2010-2011
     29 |     2 | 2011 | Première session extraordinaire de 2011-2012
     31 |     1 | 2012 | 2012-2013
     36 |     2 | 2013 | Première session extraordinaire de 2013-2014
     37 |     1 | 2014 | 2014-2015
     38 |     3 | 2013 | Seconde session extraordinaire de 2013-2014
      1 |     1 | 1999 | 1999-2000
      2 |     1 | 2000 | 2000-2001
      3 |     1 | 2001 | 2001-2002
      4 |     2 | 2001 | Première session extraordinaire de 2001-2002
      5 |     1 | 2002 | 2002-2003
      8 |     1 | 2003 | 2003-2004
      7 |     2 | 2002 | Première session extraordinaire de 2002-2003
      9 |     2 | 2003 | Première session extraordinaire de 2003-2004
     10 |     1 | 2004 | 2004-2005
     11 |     2 | 2004 | Première session extraordinaire de 2004-2005
     12 |     1 | 2005 | 2005-2006
     13 |     1 | 1996 | 1996-1997
     14 |     2 | 2005 | Première session extraordinaire de 2005-2006
     15 |     1 | 2006 | 2006-2007
     19 |     2 | 2007 | Première session extraordinaire de 2007-2008
     21 |     2 | 2008 | Session extraordinaire de 2008-2009
     23 |     2 | 2009 | Session extraordinaire de  2009-2010
     16 |     2 | 2006 | Première session extraordinaire de 2006-2007
     22 |     1 | 2009 | 2009-2010
     20 |     1 | 2008 | 2008-2009
     17 |     3 | 2006 | Deuxième session extraordinaire 2006-2007
     18 |     1 | 2007 | 2007-2008
     25 |     1 | 2010 | 2010-2011
     32 |     2 | 2012 | Première session extraordinaire de 2012-2013
     24 |     3 | 2009 | Seconde session extraordinaire 2009-2010
     28 |     1 | 2011 | 2011-2012
     33 |     3 | 2012 | Seconde session extraordinaire de 2012-2013
     34 |     4 | 2012 | Troisième session extraordinaire de 2012-2013
     30 |     3 | 2011 | Seconde session extraordinaire de 2011-2012
    """
    ann = BigIntegerField()
    lil = CharField()
    typid = ForeignKeyField(db_column='typid', rel_model=Typses, to_field='id')

    class Meta:
        db_table = 'ses'


class Fbu(BaseModel):
    """
    Mission / compte spécial / budget
    """
    lib = CharField()
    lic = CharField()
    sesid = ForeignKeyField(db_column='sesid', rel_model=Ses, to_field='id')

    class Meta:
        db_table = 'fbu'


class LecAmeli(BaseModel):
    """
     id |            lib             | lecpreid
    ----+----------------------------+----------
      1 | 1ère lecture               |
      2 | 2ème lecture               |        1
      3 | Commission Mixte Paritaire |
      4 | Nouvelle lecture           |        2
      5 | 3ème lecture               |        2
      6 | 4ème lecture               |        5
      7 | 5ème lecture               |        6
      8 | 6ème lecture               |        7
    """
    lecpreid = ForeignKeyField(db_column='lecpreid', null=True, rel_model='self', to_field='id')
    lib = CharField()

    class Meta:
        db_table = 'lec_ameli'


class Nat(BaseModel):
    """
     id |                 lib
    ----+--------------------------------------
      1 | Projet de loi
      2 | Proposition de loi
      3 | Proposition de résolution
      4 | Projet de loi organique
      5 | Projet de loi constitutionnelle
      6 | Nouvelle délibération
      7 | Proposition de loi organique
      8 | Proposition de loi constitutionnelle
      9 | Motion référendaire
    """
    lib = CharField()

    class Meta:
        db_table = 'nat'


class TxtAmeli(BaseModel):
    datado = DateTimeField(null=True)
    datdep = DateTimeField()
    dis = CharField()
    doslegsignet = CharField(null=True)
    fbuid = ForeignKeyField(db_column='fbuid', null=True, rel_model=Fbu, to_field='id')
    inl = CharField(null=True)
    int = CharField()
    lecid = ForeignKeyField(db_column='lecid', rel_model=LecAmeli, to_field='id')
    libcplnat = CharField(null=True)
    libdelim = CharField(null=True)
    loifin = CharField()
    loifinpar = BigIntegerField(null=True)
    natid = ForeignKeyField(db_column='natid', rel_model=Nat, to_field='id')
    num = CharField()
    numabs = IntegerField(index=True, null=True)
    numado = BigIntegerField(null=True)
    ordsnddelib = CharField(null=True)
    proacc = CharField()
    pubdellim = DateTimeField(null=True)
    secdel = CharField()
    sesdepid = ForeignKeyField(db_column='sesdepid', rel_model=Ses, to_field='id')
    sesinsid = ForeignKeyField(db_column='sesinsid', null=True, rel_model=Ses, related_name='ses_sesinsid_set', to_field='id')
    txtamd = CharField()
    txtetaid = ForeignKeyField(db_column='txtetaid', rel_model=Etatxt, to_field='id')
    txtexa = CharField(null=True)
    txttyp = CharField()
    urg = CharField()

    class Meta:
        db_table = 'txt_ameli'

class Typsub(BaseModel):
    lib = CharField()

    class Meta:
        db_table = 'typsub'

class Sub(BaseModel):
    dupl = CharField()
    lib = CharField(null=True)
    lic = CharField(null=True)
    merid = ForeignKeyField(db_column='merid', null=True, rel_model='self', to_field='id')
    pos = BigIntegerField(null=True)
    posder = BigIntegerField(null=True)
    prires = BigIntegerField(null=True)
    sig = CharField(null=True)
    sorid = CharField(null=True)
    subamd = CharField()
    txtid = ForeignKeyField(db_column='txtid', rel_model=TxtAmeli, to_field='id')
    typid = ForeignKeyField(db_column='typid', null=True, rel_model=Typsub, to_field='id')

    class Meta:
        db_table = 'sub'

class Typrect(BaseModel):
    lib = CharField()
    ord = BigIntegerField()

    class Meta:
        db_table = 'typrect'

class Amd(BaseModel):
    accgou = CharField(null=True)
    alinea = IntegerField(null=True)
    amdperid = ForeignKeyField(db_column='amdperid', null=True, rel_model='self', to_field='id')
    autext = CharField()
    avcid = ForeignKeyField(db_column='avcid', null=True, rel_model=Avicom, to_field='id')
    avgid = ForeignKeyField(db_column='avgid', null=True, rel_model=Avigvt, to_field='id')
    colleg = CharField()
    datdep = DateTimeField(null=True)
    dis = TextField(null=True)
    discomid = ForeignKeyField(db_column='discomid', null=True, rel_model=Discom, to_field='id')
    etaid = IntegerField(index=True)
    ideid = ForeignKeyField(db_column='ideid', null=True, rel_model=Ideamd, to_field='id')
    irrid = ForeignKeyField(db_column='irrid', null=True, rel_model=Irr, to_field='id')
    islu = CharField(null=True)
    libgrp = CharField(null=True)
    mot = CharField(null=True)
    motid = ForeignKeyField(db_column='motid', null=True, rel_model=Mot, to_field='id')
    nomentid = ForeignKeyField(db_column='nomentid', rel_model=Ent, to_field='id')
    num = CharField(null=True)
    numabs = BigIntegerField(null=True)
    obj = TextField(null=True)
    obs = CharField(null=True)
    ocmid = ForeignKeyField(db_column='ocmid', null=True, rel_model=Ent, related_name='ent_ocmid_set', to_field='id')
    opmid = ForeignKeyField(db_column='opmid', null=True, rel_model=Ent, related_name='ent_opmid_set', to_field='id')
    ord = BigIntegerField(null=True)
    rev = BigIntegerField()
    sorid = ForeignKeyField(db_column='sorid', null=True, rel_model=Sor, to_field='id')
    subid = ForeignKeyField(db_column='subid', null=True, rel_model=Sub, to_field='id')
    subidder = ForeignKeyField(db_column='subidder', null=True, rel_model=Sub, related_name='sub_subidder_set', to_field='id')
    subpos = BigIntegerField(null=True)
    txtid = ForeignKeyField(db_column='txtid', rel_model=TxtAmeli, to_field='id')
    typ = CharField()
    typrectid = ForeignKeyField(db_column='typrectid', null=True, rel_model=Typrect, to_field='id')

    class Meta:
        db_table = 'amd'

class ComAmeli(BaseModel):
    cod = CharField()
    codint = CharField()
    entid = ForeignKeyField(db_column='entid', primary_key=True, rel_model=Ent, to_field='id')
    lib = CharField()
    lil = CharField()
    spc = CharField()
    tri = BigIntegerField(null=True)

    class Meta:
        db_table = 'com_ameli'

class GrppolAmeli(BaseModel):
    cod = CharField()
    codint = CharField()
    entid = ForeignKeyField(db_column='entid', primary_key=True, rel_model=Ent, to_field='id')
    libcou = CharField()
    lilcou = CharField()
    tri = BigIntegerField(null=True)

    class Meta:
        db_table = 'grppol_ameli'

class SenAmeli(BaseModel):
    app = CharField(null=True)
    comid = ForeignKeyField(db_column='comid', null=True, rel_model=ComAmeli, to_field='entid')
    comspcid = ForeignKeyField(db_column='comspcid', null=True, rel_model=ComAmeli, related_name='com_ameli_comspcid_set', to_field='entid')
    entid = ForeignKeyField(db_column='entid', primary_key=True, rel_model=Ent, to_field='id')
    grpid = ForeignKeyField(db_column='grpid', rel_model=GrppolAmeli, to_field='entid')
    hom = CharField(null=True)
    mat = CharField()
    nomtec = CharField(null=True)
    nomuse = CharField()
    nomusemin = CharField()
    prenomuse = CharField()
    qua = CharField()
    ratt = CharField(null=True)
    senfem = CharField(null=True)

    class Meta:
        db_table = 'sen_ameli'

class Amdsen(BaseModel):
    amdid = ForeignKeyField(db_column='amdid', rel_model=Amd, to_field='id')
    hom = CharField(null=True)
    nomuse = CharField(null=True)
    prenomuse = CharField(null=True)
    qua = CharField(null=True)
    rng = BigIntegerField(null=True)
    senid = ForeignKeyField(db_column='senid', rel_model=SenAmeli, to_field='entid')

    class Meta:
        db_table = 'amdsen'
        indexes = (
            (('amdid', 'senid'), True),
        )
        primary_key = CompositeKey('amdid', 'senid')

class Cab(BaseModel):
    codint = CharField()
    entid = ForeignKeyField(db_column='entid', primary_key=True, rel_model=Ent, to_field='id')
    lil = CharField(null=True)

    class Meta:
        db_table = 'cab'

class Gvt(BaseModel):
    entid = ForeignKeyField(db_column='entid', primary_key=True, rel_model=Ent, to_field='id')
    nom = CharField()
    pre = CharField()
    qua = CharField()
    tit = CharField()

    class Meta:
        db_table = 'gvt'

class Orarol(BaseModel):
    cod = CharField(primary_key=True)
    entreq = CharField()
    lib = CharField(null=True)

    class Meta:
        db_table = 'orarol'

class Sea(BaseModel):
    dat = DateTimeField(null=True)
    num = BigIntegerField(null=True)
    sesid = ForeignKeyField(db_column='sesid', rel_model=Ses, to_field='id')

    class Meta:
        db_table = 'sea'

class Intora(BaseModel):
    entid = ForeignKeyField(db_column='entid', rel_model=Ent, to_field='id')
    entid2 = ForeignKeyField(db_column='entid2', null=True, rel_model=Ent, related_name='ent_entid2_set', to_field='id')
    mom = CharField()
    ord = BigIntegerField()
    rolcod = ForeignKeyField(db_column='rolcod', rel_model=Orarol, to_field='cod')
    seaid = ForeignKeyField(db_column='seaid', null=True, rel_model=Sea, to_field='id')
    subid = ForeignKeyField(db_column='subid', null=True, rel_model=Sub, to_field='id')
    temps = IntegerField()
    txtid = ForeignKeyField(db_column='txtid', rel_model=TxtAmeli, to_field='id')

    class Meta:
        db_table = 'intora'

class Sai(BaseModel):
    comid = ForeignKeyField(db_column='comid', rel_model=ComAmeli, to_field='entid')
    numrap = BigIntegerField(null=True)
    saityp = CharField()
    sesid = ForeignKeyField(db_column='sesid', rel_model=Ses, to_field='id')
    txtid = ForeignKeyField(db_column='txtid', rel_model=TxtAmeli, to_field='id')

    class Meta:
        db_table = 'sai'

class Saisen(BaseModel):
    id = ForeignKeyField(db_column='id', rel_model=Sai, to_field='id')
    ord = BigIntegerField()
    senid = ForeignKeyField(db_column='senid', rel_model=SenAmeli, to_field='entid')

    class Meta:
        db_table = 'saisen'
        indexes = (
            (('id', 'senid'), True),
        )
        primary_key = CompositeKey('id', 'senid')

class WNivrec(BaseModel):
    lib = CharField(null=True)
    num = BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'w_nivrec'


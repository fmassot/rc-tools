# -*- coding: utf-8 -*-

from peewee import (
    MySQLDatabase, Model, BigIntegerField, DateTimeField, CharField, TextField, DateField, CompositeKey,
    IntegerField, ForeignKeyField
)

from .db import mysql_db

database = MySQLDatabase(mysql_db['db'], **mysql_db['kwargs'])


class BaseModel(Model):
    class Meta:
        database = database


class Alinea(BaseModel):
    id = BigIntegerField(primary_key=True)
    article_loi_id = BigIntegerField(null=True)
    created_at = DateTimeField()
    nb_commentaires = BigIntegerField(null=True)
    numero = BigIntegerField(null=True)
    ref_loi = CharField(null=True)
    texte = TextField(null=True)
    texteloi_id = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'alinea'


class Amendement(BaseModel):
    id = BigIntegerField(primary_key=True)
    content_md5 = CharField(null=True)
    created_at = DateTimeField()
    date = DateField(null=True)
    expose = TextField(null=True)
    legislature = BigIntegerField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    nb_multiples = BigIntegerField(null=True)
    numero = CharField(null=True)
    rectif = BigIntegerField(null=True)
    signataires = TextField(null=True)
    sort = CharField(null=True)
    source = CharField(null=True)
    sous_amendement_de = CharField(null=True)
    sujet = CharField(null=True)
    texte = TextField(null=True)
    texteloi_id = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'amendement'


class Article(BaseModel):
    id = BigIntegerField(primary_key=True)
    article_id = BigIntegerField(null=True)
    categorie = CharField(index=True, null=True)
    citoyen_id = BigIntegerField(null=True)
    corps = TextField(null=True)
    created_at = DateTimeField()
    link = CharField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    object_id = BigIntegerField(null=True)
    slug = CharField(null=True, unique=True)
    status = CharField(null=True)
    titre = CharField(null=True)
    updated_at = DateTimeField()
    user_corps = TextField(null=True)
    version = BigIntegerField(null=True)

    class Meta:
        db_table = 'article'


class ArticleLoi(BaseModel):
    id = BigIntegerField(primary_key=True)
    expose = TextField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    ordre = BigIntegerField(null=True)
    precedent = CharField(null=True)
    slug = CharField(null=True)
    suivant = CharField(null=True)
    texteloi_id = CharField(null=True)
    titre = CharField(null=True)
    titre_loi_id = BigIntegerField(null=True)

    class Meta:
        db_table = 'article_loi'


class ArticleVersion(BaseModel):
    id = BigIntegerField()
    version = BigIntegerField()
    article_id = BigIntegerField(null=True)
    categorie = CharField(null=True)
    citoyen_id = BigIntegerField(null=True)
    corps = TextField(null=True)
    created_at = DateTimeField()
    link = CharField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    object_id = BigIntegerField(null=True)
    status = CharField(null=True)
    titre = CharField(null=True)
    updated_at = DateTimeField()
    user_corps = TextField(null=True)

    class Meta:
        db_table = 'article_version'
        primary_key = CompositeKey('id', 'version')


class Intervention(BaseModel):
    id = BigIntegerField(primary_key=True)
    created_at = DateTimeField()
    date = DateField(index=True, null=True)
    fonction = TextField(null=True)
    intervention = TextField(index=True, null=True)
    md5 = CharField(null=True, unique=True)
    nb_commentaires = BigIntegerField(null=True)
    nb_mots = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(null=True)
    personnalite_id = BigIntegerField(null=True)
    seance_id = BigIntegerField(null=True)
    section_id = BigIntegerField(null=True)
    source = CharField(null=True)
    timestamp = BigIntegerField(null=True)
    type = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'intervention'


class Organisme(BaseModel):
    id = BigIntegerField(primary_key=True)
    created_at = DateTimeField()
    nom = CharField(null=True, unique=True)
    slug = CharField(null=True, unique=True)
    type = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'organisme'


class Parlementaire(BaseModel):
    id = BigIntegerField(primary_key=True)
    id_an = BigIntegerField(null=True, unique=True)
    adresses = TextField(null=True)
    anciens_autres_mandats = TextField(null=True)
    anciens_mandats = TextField(null=True)
    autoflip = IntegerField(null=True)
    autres_mandats = TextField(null=True)
    created_at = DateTimeField()
    date_naissance = DateField(null=True)
    debut_mandat = DateField(null=True)
    fin_mandat = DateField(null=True)
    groupe_acronyme = CharField(null=True)
    lieu_naissance = CharField(null=True)
    mails = TextField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    nom = CharField(null=True)
    nom_circo = CharField(null=True)
    nom_de_famille = CharField(null=True)
    num_circo = BigIntegerField(null=True)
    parti = CharField(null=True)
    place_hemicycle = BigIntegerField(null=True)
    profession = CharField(null=True)
    sexe = CharField(null=True)
    sites_web = TextField(null=True)
    slug = CharField(null=True, unique=True)
    suppleant_de_id = BigIntegerField(null=True)
    top = TextField(null=True)
    type = CharField(null=True)
    updated_at = DateTimeField()
    url_an = CharField(null=True, unique=True)
    url_ancien_cpc = TextField(null=True)
    url_nouveau_cpc = TextField(null=True)
    villes = TextField(null=True)

    class Meta:
        db_table = 'parlementaire'


class ParlementaireAmendement(BaseModel):
    id = BigIntegerField(primary_key=True)
    amendement_id = CharField(null=True)
    created_at = DateTimeField()
    numero_signataire = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'parlementaire_amendement'


class ParlementaireOrganisme(BaseModel):
    organisme_id = ForeignKeyField(Organisme)
    parlementaire_id = ForeignKeyField(Parlementaire)
    debut_fonction = DateField(null=True)
    fonction = TextField(null=True)
    importance = BigIntegerField(null=True)

    class Meta:
        db_table = 'parlementaire_organisme'
        primary_key = CompositeKey('organisme_id', 'parlementaire_id')


class ParlementairePhoto(BaseModel):
    id = BigIntegerField(primary_key=True)
    photo = TextField(null=True)
    slug = CharField(null=True)

    class Meta:
        db_table = 'parlementaire_photo'


class ParlementaireTexteloi(BaseModel):
    id = BigIntegerField(primary_key=True)
    created_at = DateTimeField()
    fonction = CharField(null=True)
    importance = BigIntegerField(null=True)
    parlementaire = BigIntegerField(db_column='parlementaire_id', index=True, null=True)
    texteloi = CharField(db_column='texteloi_id', index=True, null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'parlementaire_texteloi'


class Personnalite(BaseModel):
    id = BigIntegerField(primary_key=True)
    created_at = DateTimeField()
    date_naissance = DateField(null=True)
    lieu_naissance = CharField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    nom = CharField(null=True)
    nom_de_famille = CharField(null=True)
    sexe = CharField(null=True)
    slug = CharField(null=True, unique=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'personnalite'


class Presence(BaseModel):
    id = BigIntegerField(primary_key=True)
    created_at = DateTimeField()
    date = DateField(null=True)
    nb_preuves = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(null=True)
    seance_id = BigIntegerField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'presence'


class PreuvePresence(BaseModel):
    id = BigIntegerField(primary_key=True)
    created_at = DateTimeField()
    presence_id = BigIntegerField(null=True)
    source = CharField(null=True)
    type = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'preuve_presence'


class QuestionEcrite(BaseModel):
    id = BigIntegerField(primary_key=True)
    content_md5 = CharField(null=True)
    created_at = DateTimeField()
    date = DateField(index=True, null=True)
    date_cloture = DateField(null=True)
    legislature = BigIntegerField(null=True)
    ministere = TextField(null=True)
    motif_retrait = TextField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    numero = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(null=True)
    question = TextField(null=True)
    reponse = TextField(null=True)
    source = CharField(null=True, unique=True)
    themes = TextField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'question_ecrite'


class Seance(BaseModel):
    annee = BigIntegerField(index=True, null=True)
    created_at = DateTimeField()
    date = DateField(null=True)
    id = BigIntegerField(primary_key=True)
    moment = CharField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    numero_semaine = BigIntegerField(null=True)
    organisme_id = BigIntegerField(null=True)
    session = CharField(index=True, null=True)
    tagged = IntegerField(null=True)
    type = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'seance'


class Section(BaseModel):
    created_at = DateTimeField()
    id = BigIntegerField(primary_key=True)
    id_dossier_an = CharField(null=True)
    max_date = DateField(null=True)
    md5 = CharField(null=True, unique=True)
    min_date = CharField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    nb_interventions = BigIntegerField(null=True)
    section_id = BigIntegerField(null=True)
    timestamp = BigIntegerField(null=True)
    titre = TextField(null=True)
    titre_complet = TextField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'section'


class Tag(BaseModel):
    id = BigIntegerField(primary_key=True)
    is_triple = IntegerField(null=True)
    name = CharField(index=True, null=True)
    triple_key = CharField(index=True, null=True)
    triple_namespace = CharField(index=True, null=True)
    triple_value = CharField(index=True, null=True)

    class Meta:
        db_table = 'tag'


class Tagging(BaseModel):
    id = BigIntegerField(primary_key=True)
    tag_id = BigIntegerField(index=True)
    taggable_id = BigIntegerField(null=True)
    taggable_model = CharField(null=True)

    class Meta:
        db_table = 'tagging'


class Texteloi(BaseModel):
    annexe = CharField(null=True)
    categorie = CharField(null=True)
    contenu = TextField(null=True)
    created_at = DateTimeField()
    date = DateField(index=True, null=True)
    id = CharField(null=True, unique=True)
    id_dossier_an = CharField(index=True, null=True)
    legislature = BigIntegerField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    numero = BigIntegerField(null=True)
    organisme_id = BigIntegerField(null=True)
    signataires = TextField(null=True)
    source = CharField(null=True, unique=True)
    titre = TextField(null=True)
    type = CharField(null=True)
    type_details = TextField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'texteloi'


class TitreLoi(BaseModel):
    created_at = DateTimeField()
    date = DateField(null=True)
    expose = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    level1 = CharField(null=True)
    level2 = CharField(null=True)
    level3 = CharField(null=True)
    level4 = CharField(null=True)
    leveltype = CharField(null=True)
    nb_articles = BigIntegerField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(null=True)
    source = CharField(null=True, unique=True)
    texteloi_id = CharField(null=True)
    titre = TextField(null=True)
    titre_loi_id = BigIntegerField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'titre_loi'


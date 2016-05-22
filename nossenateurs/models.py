# -*- coding: utf-8 -*-

from peewee import (
    MySQLDatabase, Model, BigIntegerField, DateTimeField, CharField, TextField, DateField, CompositeKey, IntegerField
)

from .db import mysql_db

database = MySQLDatabase(mysql_db['db'], **mysql_db['kwargs'])


class UnknownField(object):
    pass


class BaseModel(Model):
    class Meta:
        database = database


class Alinea(BaseModel):
    article_loi_id = BigIntegerField(db_column='article_loi_id', index=True, null=True)
    created_at = DateTimeField()
    id = BigIntegerField(primary_key=True)
    nb_commentaires = BigIntegerField(null=True)
    numero = BigIntegerField(null=True)
    ref_loi = CharField(null=True)
    texte = TextField(null=True)
    texteloi_id = CharField(db_column='texteloi_id', index=True, null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'alinea'
        indexes = (
            (('texteloi', 'article_loi_id', 'numero'), True),
        )


class Amendement(BaseModel):
    avis_comm = CharField(null=True)
    avis_gouv = CharField(null=True)
    content_md5 = CharField(null=True)
    created_at = DateTimeField()
    date = DateField(null=True)
    expose = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    nb_commentaires = BigIntegerField(null=True)
    numero = CharField(null=True)
    numero_pere = BigIntegerField(null=True)
    organisme_id = BigIntegerField(index=True, null=True)
    rectif = BigIntegerField(null=True)
    ref_loi = CharField(null=True)
    signataires = TextField(null=True)
    sort = CharField(null=True)
    source = CharField(null=True)
    sujet = CharField(null=True)
    texte = TextField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'amendement'
        indexes = (
            (('sujet', 'texte', 'expose'), False),
            (('texteloi', 'numero', 'rectif'), True),
        )


class Article(BaseModel):
    article_id = BigIntegerField(index=True, null=True)
    categorie = CharField(index=True, null=True)
    citoyen_id = BigIntegerField(index=True, null=True)
    corps = TextField(null=True)
    created_at = DateTimeField()
    id = BigIntegerField(primary_key=True)
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
        indexes = (
            (('categorie', 'object'), False),
            (('categorie', 'titre'), False),
            (('categorie', 'titre', 'citoyen_id'), False),
        )


class ArticleLoi(BaseModel):
    expose = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    nb_commentaires = BigIntegerField(null=True)
    ordre = BigIntegerField(null=True)
    precedent = CharField(null=True)
    slug = CharField(null=True)
    suivant = CharField(null=True)
    texteloi_id = CharField(index=True, null=True)
    titre = CharField(null=True)
    titre_loi_id = BigIntegerField(index=True, null=True)

    class Meta:
        db_table = 'article_loi'
        indexes = (
            (('texteloi_id', 'ordre'), False),
            (('texteloi_id', 'titre'), True),
        )


class ArticleVersion(BaseModel):
    article_id = BigIntegerField(null=True)
    categorie = CharField(null=True)
    citoyen_id = BigIntegerField(null=True)
    corps = TextField(null=True)
    created_at = DateTimeField()
    id = BigIntegerField()
    link = CharField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    object_id = BigIntegerField(null=True)
    status = CharField(null=True)
    titre = CharField(null=True)
    updated_at = DateTimeField()
    user_corps = TextField(null=True)
    version = BigIntegerField()

    class Meta:
        db_table = 'article_version'
        indexes = (
            (('id', 'version'), True),
        )
        primary_key = CompositeKey('id', 'version')


class Intervention(BaseModel):
    created_at = DateTimeField()
    date = DateField(index=True, null=True)
    fonction = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    intervention = TextField(index=True, null=True)
    md5 = CharField(null=True, unique=True)
    nb_commentaires = BigIntegerField(null=True)
    nb_mots = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(index=True, null=True)
    personnalite_id = BigIntegerField(index=True, null=True)
    seance_id = BigIntegerField(index=True, null=True)
    section_id = BigIntegerField(index=True, null=True)
    source = CharField(null=True)
    timestamp = BigIntegerField(null=True)
    type = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'intervention'


class Organisme(BaseModel):
    created_at = DateTimeField()
    id = BigIntegerField(primary_key=True)
    nom = CharField(null=True, unique=True)
    slug = CharField(null=True, unique=True)
    type = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'organisme'


class Parlementaire(BaseModel):
    adresses = TextField(null=True)
    anciens_mandats = TextField(null=True)
    autoflip = IntegerField(null=True)
    autres_mandats = TextField(null=True)
    created_at = DateTimeField()
    date_naissance = DateField(null=True)
    debut_mandat = DateField(null=True)
    fin_mandat = DateField(null=True)
    groupe_acronyme = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    id_institution = CharField(null=True, unique=True)
    mails = TextField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    nom = CharField(null=True)
    nom_circo = CharField(null=True)
    nom_de_famille = CharField(null=True)
    num_circo = BigIntegerField(null=True)
    parti = CharField()
    place_hemicycle = BigIntegerField(null=True)
    profession = CharField(null=True)
    sexe = CharField(null=True)
    sites_web = TextField(null=True)
    slug = CharField(null=True, unique=True)
    suppleant_de_id = BigIntegerField(index=True, null=True)
    top = TextField(null=True)
    type = CharField(null=True)
    updated_at = DateTimeField()
    url_institution = CharField(null=True, unique=True)
    villes = TextField(null=True)

    class Meta:
        db_table = 'parlementaire'


class ParlementaireAmendement(BaseModel):
    amendement_id = CharField(index=True, null=True)
    created_at = DateTimeField()
    id = BigIntegerField(primary_key=True)
    numero_signataire = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(index=True, null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'parlementaire_amendement'


class ParlementaireOrganisme(BaseModel):
    debut_fonction = DateField(null=True)
    fonction = TextField(null=True)
    importance = BigIntegerField(null=True)
    organisme_id = BigIntegerField()
    parlementaire_id = BigIntegerField(index=True)

    class Meta:
        db_table = 'parlementaire_organisme'
        indexes = (
            (('organisme_id', 'parlementaire_id'), True),
        )
        primary_key = CompositeKey('organisme_id', 'parlementaire_id')


class ParlementairePhoto(BaseModel):
    id = BigIntegerField(primary_key=True)
    photo = TextField(null=True)
    slug = CharField(null=True)

    class Meta:
        db_table = 'parlementaire_photo'


class ParlementaireTexteloi(BaseModel):
    created_at = DateTimeField()
    fonction = CharField(null=True)
    id = BigIntegerField(primary_key=True)
    importance = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(db_column='parlementaire_id', index=True, null=True)
    texteloi_id = CharField(db_column='texteloi_id', index=True, null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'parlementaire_texteloi'


class Personnalite(BaseModel):
    created_at = DateTimeField()
    date_naissance = DateField(null=True)
    id = BigIntegerField(primary_key=True)
    nb_commentaires = BigIntegerField(null=True)
    nom = CharField(null=True)
    nom_de_famille = CharField(null=True)
    sexe = CharField(null=True)
    slug = CharField(null=True, unique=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'personnalite'


class Presence(BaseModel):
    created_at = DateTimeField()
    date = DateField(null=True)
    id = BigIntegerField(primary_key=True)
    nb_preuves = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(index=True, null=True)
    seance_id = BigIntegerField(index=True, null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'presence'


class PreuvePresence(BaseModel):
    created_at = DateTimeField()
    id = BigIntegerField(primary_key=True)
    presence_id = BigIntegerField(index=True, null=True)
    source = CharField(null=True)
    type = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'preuve_presence'


class Question(BaseModel):
    content_md5 = CharField(null=True)
    created_at = DateTimeField()
    date = DateField(null=True)
    date_cloture = DateField(null=True)
    id = BigIntegerField(primary_key=True)
    legislature = BigIntegerField(null=True)
    ministere = TextField(null=True)
    motif_retrait = TextField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    numero = CharField(null=True)
    parlementaire_id = BigIntegerField(index=True, null=True)
    question = TextField(null=True)
    reponse = TextField(null=True)
    source = CharField(null=True, unique=True)
    titre = TextField(null=True)
    type = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'question'
        indexes = (
            (('legislature', 'numero'), True),
        )


class Seance(BaseModel):
    annee = BigIntegerField(index=True, null=True)
    created_at = DateTimeField()
    date = DateField(null=True)
    id = BigIntegerField(primary_key=True)
    moment = CharField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    numero_semaine = BigIntegerField(null=True)
    organisme_id = BigIntegerField(index=True, null=True)
    session = CharField(index=True, null=True)
    tagged = IntegerField(null=True)
    type = CharField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'seance'
        indexes = (
            (('annee', 'numero_semaine'), False),
            (('organisme_id', 'date', 'moment'), True),
        )


class Section(BaseModel):
    created_at = DateTimeField()
    id = BigIntegerField(primary_key=True)
    id_dossier_institution = CharField(null=True)
    max_date = DateField(null=True)
    md5 = CharField(null=True, unique=True)
    min_date = CharField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    nb_interventions = BigIntegerField(null=True)
    section_id = BigIntegerField(index=True, null=True)
    timestamp = BigIntegerField(null=True)
    titre = TextField(null=True)
    titre_complet = TextField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'section'


class Tag(BaseModel):
    id = BigIntegerField(primary_key=True)
    is_triple = IntegerField(index=True, null=True)
    name = CharField(index=True, null=True)
    triple_key = CharField(index=True, null=True)
    triple_namespace = CharField(index=True, null=True)
    triple_value = CharField(index=True, null=True)

    class Meta:
        db_table = 'tag'


class Tagging(BaseModel):
    id = BigIntegerField(primary_key=True)
    tag_id = BigIntegerField(db_column='tag_id', index=True)
    taggable_id = CharField(db_column='taggable_id', null=True)
    taggable_model = CharField(index=True, null=True)

    class Meta:
        db_table = 'tagging'
        indexes = (
            (('taggable_model', 'taggable_id'), False),
        )


class Texteloi(BaseModel):
    annexe = CharField(null=True)
    categorie = CharField(null=True)
    contenu = TextField(null=True)
    created_at = DateTimeField()
    date = DateField(index=True, null=True)
    id = CharField(null=True, unique=True)
    id_dossier_institution = CharField(index=True, null=True)
    nb_commentaires = BigIntegerField(null=True)
    numero = BigIntegerField(null=True)
    organisme_id = BigIntegerField(index=True, null=True)
    signataires = TextField(null=True)
    source = CharField(null=True, unique=True)
    titre = TextField(null=True)
    type = CharField(null=True)
    type_details = TextField(null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'texteloi'
        indexes = (
            (('numero', 'annexe'), False),
            (('type', 'type_details'), False),
        )


class TitreLoi(BaseModel):
    """
    Empty table
    """
    chapitre = CharField(null=True)
    created_at = DateTimeField()
    date = DateField(null=True)
    expose = TextField(null=True)
    id = BigIntegerField(primary_key=True)
    nb_articles = BigIntegerField(null=True)
    nb_commentaires = BigIntegerField(null=True)
    parlementaire_id = BigIntegerField(index=True, null=True)
    section = CharField(null=True)
    source = CharField(null=True, unique=True)
    texteloi_id = CharField(index=True, null=True)
    titre = TextField(null=True)
    titre_loi_id = BigIntegerField(index=True, null=True)
    updated_at = DateTimeField()

    class Meta:
        db_table = 'titre_loi'


class VariableGlobale(BaseModel):
    champ = CharField(null=True)
    created_at = DateTimeField()
    id = BigIntegerField(primary_key=True)
    updated_at = DateTimeField()
    value = TextField(null=True)

    class Meta:
        db_table = 'variable_globale'


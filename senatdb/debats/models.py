from peewee import *

database = PostgresqlDatabase('debats', **{})


class UnknownField(object):
    pass


class BaseModel(Model):
    class Meta:
        database = database


class Debats(BaseModel):
    autinc = CharField(null=True)
    datsea = DateTimeField(primary_key=True)
    debsyn = CharField(null=True)
    deburl = CharField(null=True)
    estcongres = CharField(null=True)
    libspec = CharField(null=True)
    numero = BigIntegerField(null=True)

    class Meta:
        db_table = 'debats'


class Intdivers(BaseModel):
    autcod = CharField(index=True)
    intana = CharField(null=True)
    intdiverscle = BigIntegerField(primary_key=True)
    intdiversordid = BigIntegerField(null=True)
    intfon = CharField(null=True)
    inturl = CharField(null=True)
    secdiverscle = BigIntegerField(index=True)

    class Meta:
        db_table = 'intdivers'


class Intpjl(BaseModel):
    autcod = CharField(index=True)
    intana = CharField(null=True)
    intfon = CharField(null=True)
    intordid = BigIntegerField(null=True)
    intpjlcle = BigIntegerField(primary_key=True)
    inturl = CharField(null=True)
    secdiscle = BigIntegerField(index=True)

    class Meta:
        db_table = 'intpjl'


class Lecassdeb(BaseModel):
    datsea = DateTimeField(index=True)
    lecassidt = CharField(index=True)

    class Meta:
        db_table = 'lecassdeb'
        indexes = (
            (('lecassidt', 'datsea'), True),
        )
        primary_key = CompositeKey('datsea', 'lecassidt')


class Typsec(BaseModel):
    typseccat = CharField(null=True)
    typseccod = CharField(primary_key=True)
    typseclib = CharField()

    class Meta:
        db_table = 'typsec'


class Secdis(BaseModel):
    datsea = DateTimeField(index=True)
    lecassidt = CharField(index=True)
    secdiscle = BigIntegerField(primary_key=True)
    secdisnum = CharField(null=True)
    secdisobj = CharField(null=True)
    secdisordid = BigIntegerField(null=True)
    secdispere = BigIntegerField(index=True, null=True)
    secdisurl = CharField(null=True)
    typseccod = ForeignKeyField(db_column='typseccod', rel_model=Typsec, to_field='typseccod')

    class Meta:
        db_table = 'secdis'


class Secdivers(BaseModel):
    datsea = DateTimeField(index=True)
    secdiverscle = BigIntegerField(primary_key=True)
    secdiverslibelle = CharField(null=True)
    secdiversobj = CharField(null=True)
    typseccod = ForeignKeyField(db_column='typseccod', rel_model=Typsec, to_field='typseccod')

    class Meta:
        db_table = 'secdivers'


class Syndeb(BaseModel):
    debsyn = CharField(primary_key=True)
    syndeblib = CharField()

    class Meta:
        db_table = 'syndeb'


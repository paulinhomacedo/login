#--proxy http://usertrac:Fusca.Vermelho.5381@MTZSVMFCPPRD02:8080
from datetime import datetime

from peewee import (DateTimeField, ForeignKeyField, IntegerField, Model,
                    SqliteDatabase, TextField)

db = SqliteDatabase('notas.db')


class BaseModel(Model):
    class Meta:
        database = db


class Pessoa(BaseModel):
    nome = TextField()
    email = TextField(unique=True)
    senha = TextField()
    idade = IntegerField()


class Grupo(BaseModel):
    nome = TextField()
    dona = ForeignKeyField(Pessoa, backref='grupos')


class Nota(BaseModel):
    dona = ForeignKeyField(Pessoa, backref='notas')
    grupo = ForeignKeyField(Grupo, backref='notas', null=True, default=None)
    titulo = TextField()
    nota = TextField()
    criada_em = DateTimeField(default=datetime.now)
    modificada_em = DateTimeField(default=datetime.now)

db.create_tables([Pessoa,Grupo, Nota])    

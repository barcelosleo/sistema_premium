import peewee

from Database import BaseModel

class Call(BaseModel):
    id = peewee.AutoField()
    data = peewee.DateField()
    nomeUsuario = peewee.CharField()
    documento = peewee.CharField()
    laboratorio = peewee.CharField()
    equipamento = peewee.CharField()
    numeroAmostras = peewee.CharField()
    atividade = peewee.IntegerField()
    tipoUsuario = peewee.IntegerField()
    origemUsuario = peewee.IntegerField()
import peewee
from Database import db
from Model import Call


try:
    Call.create_table()
except peewee.OperationalError:
    print('Tabela Author ja existe!')
import peewee

db = peewee.SqliteDatabase('__local_database.db')

class BaseModel(peewee.Model):
    class Meta:
        database = db



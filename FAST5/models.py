from peewee import SqliteDatabase, Model, AutoField, FloatField, CharField


db = SqliteDatabase("test.db")


class Item(Model):
    id = AutoField()
    name = CharField()
    price = FloatField()
    description = CharField(null=True)

    class Meta:
        database = db

db.connect()
db.create_tables([Item])
#coding:utf-8

from peewee import *
from datetime import datetime

db = PostgresqlDatabase(
    database='my_first_blog',
    user='chao',
    password='e4728f444b24839e3f80adf3829bcba9',
    host='127.0.0.1',
    port=5432)

class Article(Model):
    class Meta:
        database = db

    title = CharField()
    description = CharField()
    creation_timestamp = DateTimeField(formats='%Y-%m-%d %H:%M:%S')
    last_updated_timestamp = DateTimeField(formats='%Y-%m-%d %H:%M:%S')
    viewed_times = IntegerField(default=0)
    commnet_times = IntegerField(default=0)
    path = CharField()

db.connect()

if __name__ == '__main__':
    for d in Article.select(Article.id, Article.creation_timestamp, Article.title):
        print(d.id, d.creation_timestamp)
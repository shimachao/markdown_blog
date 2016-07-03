#coding:utf-8

from pony.orm import Required, Database, select, commit, db_session
from pony.orm.serialization import to_dict
from datetime import datetime

db = Database()
db.bind('postgres', user='chao', password='e4728f444b24839e3f80adf3829bcba9', host='127.0.0.1', port=5432, database='my_first_blog')


class Article(db.Entity):
    title = Required(str)
    description = Required(str)
    creation_timestamp = Required(datetime)
    last_updated_timestamp = Required(datetime)
    viewed_times = Required(int, default=0)
    commnet_times = Required(int, default=0)
    path = Required(str)


db.generate_mapping()

if __name__ == '__main__':
    title='socketserver.py代码阅读笔记'
    description = """一直想弄清楚一个http server和Web框架的工作原理。但以我目前的实力，
    阅读一个http server或web框架代码还是太难了。后来又对异步IO、并发产生的兴趣。"""
    creation_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_updated_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    path = 'article\socketserver.py代码阅读笔记.md'
    with db_session:
        # 插入
        # article = Article(title=title,\
        # description=description,\
        # creation_timestamp=creation_timestamp,\
        # last_updated_timestamp=last_updated_timestamp, \
        # path=path)
        # commit()

        # 查询
        # select(a for a in Article)[:].show()
        # d = select(a for a in Article)
        # d=to_dict(d)['Article']
        # for k,v in d.items():
        #     print(v['id'], v['description'])
        #     print('\n\n')

        for d in select(a for a in Article):
            print(d.to_dict(only=['id', 'title']))
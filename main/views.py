# coding:utf-8
from flask import Flask
from db import Article

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>正在施工中...</h1><h1>施工完会看到文章列表</h1>'

@app.route('/article/<int:article_id>')
def article(article_id):
    # 返回请求的文章
    d = Article.select().where(Article.id == 2).get()
    return d.description

if __name__ == '__main__':
    app.run(debug=True)

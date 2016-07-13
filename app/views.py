# coding:utf-8
from flask import Flask
from flask import request, render_template, abort
from db import Article
from md_renderer import md
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
boot = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    return '<h1>正在施工中...</h1><h1>施工完会看到文章列表</h1>'


@app.route('/article/<int:article_id>')
def article(article_id):
    # 返回请求的文章
    d = Article.select().where(Article.id == article_id)
    print(d)
    if not d:
        abort(404)
    d = d.get()
    path = '..\\' + d.path
    file = open(file=path, mode='r', encoding='utf-8')
    text = md(file.read())
    return render_template('article.html', title=d.title,text=text)
    

if __name__ == '__main__':
    app.run(debug=True)

# coding:utf-8
from flask import Flask
from flask import request, render_template
from db import Article
from md_renderer import md

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>正在施工中...</h1><h1>施工完会看到文章列表</h1>'

@app.route('/article/<int:article_id>')
def article(article_id):
    # 返回请求的文章
    d = Article.select().where(Article.id == 2).get()
    path = '..\\' + d.path
    file = open(file=path, mode='r', encoding='utf-8')
    text = md(file.read())
    return render_template('article.html', text=text)
    # return body

@app.route('/static/img/<filename>')
def img_file(filename):
    img = open(file='../static/img/'+filename, mode='rb')
    return img.read()

@app.route('/static/css/<filename>')
def css_file(filename):
    img = open(file='../static/css/'+filename, mode='r')
    return img.read()

if __name__ == '__main__':
    app.run(debug=True)

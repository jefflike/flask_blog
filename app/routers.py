from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    '''
    视图函数中将数据渲染进模板
    :return:
    '''
    user = {'username': 'jeff'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
from flask import render_template, flash, redirect

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/ind', endpoint='index')
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 校验我们的表单数据
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
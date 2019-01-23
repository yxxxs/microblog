from flask import render_template, redirect, url_for
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'yxxxs'}
    posts = [
        {'author': {'username': 'Zhoujie'},
         'body': 'where r u'},

        {'author': {'username': 'Xiaobao'},
         'body': 'da xue lu'}
    ]

    return render_template('index.html', title = 'home', user = user, posts = posts)


@app.route('/login', methods = ['get', 'post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', title = 'sign in', form = form)
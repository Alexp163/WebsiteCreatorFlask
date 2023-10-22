from app import app
from flask import render_template
from db_run import Development


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/our_projects')
def our_projects():
    development = Development.query.all()
    return render_template('our_projects.html', development=development)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/work/1')
def type_work():
    return render_template('one_service.html')

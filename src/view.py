from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/our_projects')
def our_projects():
    return render_template('our_projects.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')

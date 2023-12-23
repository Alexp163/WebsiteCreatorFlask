from flask import render_template, flash, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import app
from db import db
from forms import LoginForm, RegisterForm
from models import Development, Service, ServiceGroup, User


@app.route('/')
def index():
    service_groups = ServiceGroup.query.all()
    return render_template('index.html', service_groups=service_groups)


@app.route('/our_projects')
@login_required
def our_projects():
    development = Development.query.all()
    return render_template('our_projects.html', development=development)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print("Кнопка нажата!!!")
        flash("Кнопка нажата")
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Авторизация успешна!!!")
        else:
            flash("Не верный логин или пароль!!!")
    return render_template('login.html', form=form)


@app.route('/registration', methods=["GET","POST"])
def registration():
    form = RegisterForm()
    if request.method=='POST' and form.validate():
        print("Кнопка нажата!!!")
        flash("Кнопка нажата")
        email = form.email.data
        pass_1 = form.password_1.data
        pass_2 = form.password_2.data
        if pass_1 == pass_2:
            if len(User.query.filter_by(email=email).all())==0:
                user = User(email=email, password_hash=generate_password_hash(pass_1))
                db.session.add(user)
                db.session.commit()
                flash("Регистрация прошла успешно!!!")
            else:
                flash("Вы уже проходили регистрацию!")
        else:
            flash("Пароли не совпадают!")
    return render_template('registration.html', form=form)


@app.route('/work/1')
@login_required
def type_work():
    return render_template('one_service.html')


@app.route('/our_service')
@login_required
def our_service():
    service = Service.query.all()
    return render_template('our_service.html', service=service)


@app.route('/service_group/<int:service_group_id>')
def service_group(service_group_id):
    service_group = ServiceGroup.query.get(service_group_id)
    service_groups = ServiceGroup.query.all()
    service = Service.query.filter_by(service_group_id=service_group_id).all()
    return render_template("service_group.html", service_group=service_group,
                           service_groups=service_groups, service=service)


@app.route('/logout')
def logout():
    logout_user()
    return render_template('index')


@app.errorhandler(401)
def custom(error):
    return render_template('error401.html')


@app.errorhandler(404)
def custom(error):
    return render_template('error404.html')


@app.errorhandler(500)
def custom(error):
    return render_template('error500.html')

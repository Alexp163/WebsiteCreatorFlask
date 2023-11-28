from app import app
from flask import render_template
from models import Development, Service, ServiceGroup
from forms import LoginForm, RegisterForm


@app.route('/')
def index():
    service_groups = ServiceGroup.query.all()
    return render_template('index.html', service_groups=service_groups)


@app.route('/our_projects')
def our_projects():
    development = Development.query.all()
    return render_template('our_projects.html', development=development)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/registration')
def registration():
    form = RegisterForm()
    return render_template('registration.html', form=form)


@app.route('/work/1')
def type_work():
    return render_template('one_service.html')


@app.route('/our_service')
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


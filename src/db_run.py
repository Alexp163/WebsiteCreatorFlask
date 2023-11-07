from db import db
from app import app
from models import Development, Service, ServiceGroup

with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    development = Development(name_product="разработка бэкэнда",
                              technology="flask",
                              date_development="10.10.2023", price="50000.00",
                              developer="Александр Попов")
    db.session.add(development)
    development1 = Development(name_product="разработка дизайна сайта",
                               technology="Photoshop",
                               date_development="12.10.2023", price="10000.00",
                               developer="Сергей Трофимов")
    db.session.add(development1)
    db.session.commit()

with app.app_context():
    group1 = ServiceGroup(name="Разработка дизайна сайта",
                          description="Здесь будет описана группа")
    group2 = ServiceGroup(name="Верстка страниц сайта",
                          description="Здесь будет описана группа")
    group3 = ServiceGroup(name="Разработка фронтенда",
                          description="Здесь будет описана группа")
    group4 = ServiceGroup(name="Разработка бэкэнда",
                          description="Здесь будет описана группа")
    db.session.add(group1)
    db.session.add(group2)
    db.session.add(group3)
    db.session.add(group4)
    db.session.commit()
    service = Service(name_product="Разработка дизайна сайта",
                      technоlogi="Photoshop", date_development="7 дней",
                      price="10000.0",
                      developer="Веб-дизайнер Иващук И.В")
    db.session.add(service)
    service1 = Service(name_product="Верстка страниц сайта",
                       technоlogi="HTML, CSS, Bootstrap",
                       date_development="10 дней", price="15000.0",
                       developer="Верстальщик Сергеев В.Ф.")
    db.session.add(service1)
    service2 = Service(name_product="Разработка фронтенда сайта",
                       technоlogi="Javascript, HTML, CSS",
                       date_development="14 дней", price="20000.0",
                       developer="Фронтенд-разработчик Сурков А.С.")
    db.session.add(service2)
    service3 = Service(name_product="Разработка бэкэнда сайта",
                       technоlogi="Python, flask", date_development="30 дней",
                       price="30000.0",
                       developer="Бэкэнд разработчик Паштиян Х.А.")
    db.session.add(service3)
    db.session.commit()

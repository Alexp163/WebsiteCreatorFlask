from db import db
from app import app
from models import Development


with app.app_context():
    db.drop_all()
    db.create_all()


with app.app_context():
    development = Development(name_product = "разработка бэкэнда", technology = "flask",
                              date_development = "10.10.2023", price = "50000.00",
                              developer = "Александр Попов")
    db.session.add(development)
    development1 = Development(name_product = "разработка дизайна сайта", technology = "Photoshop",
                              date_development = "12.10.2023", price = "10000.00",
                              developer = "Сергей Трофимов")
    db.session.add(development1)
    db.session.commit()


with app.app_context():
    development = Development.query.all()
    for d in development:
        print(d.name_product, d.price, d.developer)
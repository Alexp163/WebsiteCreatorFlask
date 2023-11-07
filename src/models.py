from db import db


# id - число name_product - наименование продукта, услуги technology -
# технология изготовления date_development - дата изготовления price -
# стоимость developer - разработчик ______________________________
# db.String(50) - текстовое поле заданной длины db.Integer() - числовое поле
# db.Column() - создание колонки(дополнительные поля: nullable-не может быть
# пустой, unique - уникальна, primary_key)
# для id всегда задается primary_key=True


class Development(db.Model):
    __tablename__ = "development"

    id = db.Column(db.Integer(), primary_key=True)  # идентификационный номер
    name_product = db.Column(db.String(20))  # наименование продукта(услуги)

    technology = db.Column(db.Text())  # технология выполнения
    date_development = db.Column(db.String(10))  # дата разработки продукта

    price = db.Column(db.Float())  # цена продукта
    developer = db.Column(db.String(20))  # разработчик


class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer(), primary_kay=True)
    name_product = db.Column(db.String(20))  # наименование продукта

    technology = db.Column(db.Text())  # технология выполнения
    date_development = db.Column(db.String(10))  # дата изготовления

    price = db.Column(db.Float())  # цена продукта
    developer = db.Column(db.String(20))  # разработчик


class ServiceGroup(db.Model):
    __tablename__ = "service_group"
    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.String(100))  # название группы
    description = db.Column(db.Text())  # описание группы
    # создать руководителя группы

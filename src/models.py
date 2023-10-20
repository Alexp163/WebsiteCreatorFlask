from db import db


# id - число
# name_product - наименование продукта, услуги
# technology - технология изготовления
# date_development - дата изготовления
# price - стоимость
# developer - разработчик
# ______________________________
# db.Strings(50) - текстовое поле заданной длины
# db.Integer() - числовое поле
# db.Column() - создание колонки(дополнительные поля: nullable-не может быть пустой, unique - уникальна, primary_key)
# для id всегда задается primary_key=True


class Development:
    __tablename__ = "development"

    id = db.Column(db.Integer(), primary_key=True) # идентификационный номер
    name_product = db.Column(db.String()) # наименование продукта(услуги)

    technology = db.Column(db.String()) # технология выполнения
    date_development = db.Column(db.String(10)) # дата разработки продукта

    price = db.Column(db.String(10)) # цена продукта
    developer = db.Column(db.String()) # разработчик

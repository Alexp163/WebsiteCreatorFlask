from db import db
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Float
from sqlalchemy.orm import Relationship
from sqlalchemy.sql import func

# id - число name_product - наименование продукта, услуги technology -
# технология изготовления date_development - дата изготовления price -
# стоимость developer - разработчик ______________________________
# db.String(50) - текстовое поле заданной длины db.Integer() - числовое поле
# db.Column() - создание колонки(дополнительные поля: nullable-не может быть
# пустой, unique - уникальна, primary_key)
# для id всегда задается primary_key=True


class Development(db.Model):
    __tablename__ = "development"

    id = Column(Integer(), primary_key=True)  # идентификационный номер
    name_product = Column(String(20))  # наименование продукта(услуги)

    technology = Column(Text())  # технология выполнения
    date_development = Column(String(10))  # дата разработки продукта

    price = Column(Float())  # цена продукта
    developer = Column(String(20))  # разработчик

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Наименование продукта: {self.name_product}, технология: {self.technology}, "
                f"дата разработки: {self.date_development}, цена: {self.price}, "
                f"разработчик: {self.developer}>")


class Service(db.Model):
    __tablename__ = 'service'
    id = Column(Integer(), primary_key=True)
    name_product = Column(String(20))  # наименование продукта

    technology = Column(Text())  # технология выполнения
    date_development = Column(String(10))  # дата изготовления

    price = Column(Float())  # цена продукта
    developer = Column(String(20))  # разработчик
    service_group_id = Column(ForeignKey("service_group.id"))  # id группы, к которой относится эта услуга
    service_group = Relationship("ServiceGroup")  # ссылка на группу(id которой указан в вышестоящей строчке)

    created_at = Column(DateTime, server_default=func.now())  # дата создания
    updated_at = Column(DateTime, server_onupdate=func.now())  # дата обновления

    def __repr__(self):
        return (f"<Наименование продукта: {self.name_product}, технология: {self.technology}, "
                f"дата разработки: {self.date_development}, цена: {self.price}, "
                f"разработчик: {self.developer}>")

class ServiceGroup(db.Model):
    __tablename__ = "service_group"
    id = Column(Integer(), primary_key=True)

    name = Column(String(100))  # название группы
    description = Column(Text())  # описание группы
    # создать руководителя группы

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_onupdate=func.now())

    def __repr__(self):
        return f"<Название группы: {self.name}, Описание группы: {self.description}>"



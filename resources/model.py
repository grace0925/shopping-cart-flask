from flask import Flask
from marshmallow import Schema, fields, pre_load, validate, ValidationError
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class List(db.Model):
    __tablename__ = 'tbl_list'
    id = db.Column(db.BIGINT, primary_key=True)
    item_name = db.Column(db.VARCHAR(45), nullable=False)
    item_quantity = db.Column(db.FLOAT, nullable=False)
    item_unit = db.Column(db.VARCHAR(45), nullable=False)
    item_done = db.Column(db.BOOLEAN)

def __init__(self, name, quantity, unit):
    self.item_name = name
    self.item_quantity = quantity
    self.item_unit = unit
    self.done = False

class ListSchema(ma.Schema):
    class Meta:
        fields("id", "item_name", "item_quantity", "item_unit", "item_done")


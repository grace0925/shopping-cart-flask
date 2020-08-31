from . import db


class Item(db.Model):
    __tablename__ = 'tbl_list'
    id = db.Column(db.BIGINT, primary_key=True)
    item_name = db.Column(db.VARCHAR(45), unique=True, nullable=False)
    item_quantity = db.Column(db.FLOAT, nullable=False)
    item_unit = db.Column(db.VARCHAR(45), nullable=False)
    item_done = db.Column(db.BOOLEAN)

    def __init__(self, name, quantity, unit):
        self.item_name = name
        self.item_quantity = quantity
        self.item_unit = unit
        self.item_done = False

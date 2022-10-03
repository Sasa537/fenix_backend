from flask_sqlalchemy import SQLAlchemy

db_catalog = SQLAlchemy()

class Catalog(db_catalog.Model):
    id = db_catalog.Column(db_catalog.Integer, primary_key=True)
    name = db_catalog.Column(db_catalog.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {"id":self.id,"name":self.name}
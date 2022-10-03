from flask_sqlalchemy import SQLAlchemy

db_podcatalog = SQLAlchemy()

class Podcatalog (db_podcatalog.Model):
    id = db_podcatalog.Column(db_podcatalog.Integer, primary_key=True)
    id_catalog = db_podcatalog.Column(db_podcatalog.Integer, nullable=False)
    name = db_podcatalog.Column(db_podcatalog.String(100), nullable=False)

    def __init__(self, id_catalog, name):
          self.id_catalog = id_catalog
          self.name = name

    def json(self):
        return {"id":self.id,"id_catalog":self.id_catalog,"name":self.name}
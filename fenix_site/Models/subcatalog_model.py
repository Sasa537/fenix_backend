from flask_sqlalchemy import SQLAlchemy

db_subcatalog = SQLAlchemy()


class Subcatalog(db_subcatalog.Model):
    id = db_subcatalog.Column(db_subcatalog.Integer, primary_key=True)
    id_catalog = db_subcatalog.Column(db_subcatalog.Integer, nullable=False)
    name = db_subcatalog.Column(db_subcatalog.String(100), nullable=False)

    def __init__(self, id_catalog, name):
        self.id_catalog = id_catalog
        self.name = name

    def json(self):
        return {"id": self.id, "id_catalog": self.id_catalog, "name": self.name}

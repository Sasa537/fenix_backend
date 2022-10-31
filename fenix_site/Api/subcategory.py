from flask import request
from fenix_site.Models.subcatalog_model import Subcatalog, db_subcatalog
from flask_restful import Resource


class Subcategory(Resource):
    def get(self, id):
        subcategory = Subcatalog.query.filter_by(id_catalog=id).all()
        return {"Subategory": list(x.json() for x in subcategory)}

    def post(self):
        data = request.get_json()
        new_subcategory = Subcatalog(data['id_catalog'], data['name'])
        db_subcatalog.session.add(new_subcategory)
        db_subcatalog.session.commit()
        return new_subcategory.json(), 201

    def put(self, id):
        data = request.get_json()
        subcategory = Subcatalog.query.filter_by(id=id).first()
        subcategory.name = data['name']
        db_subcatalog.session.add(subcategory)
        db_subcatalog.session.commit()
        return subcategory.json()

    def delete(self, id):
        subcategory = Subcatalog.query.filter_by(id=id).first()
        if subcategory:
            db_subcatalog.session.delete(subcategory)
            db_subcatalog.session.commit()
            return {"message":"deleted"}
        else:
            return {"message":"not found"}


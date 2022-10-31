from flask import request
from flask_restful import Resource
from fenix_site.Models.catalog_model import Catalog, db_catalog


class Category(Resource):
    def get(self):
        catalog = Catalog.query.all()
        return {"Category": list(x.json() for x in catalog)}

    def post(self):
        data = request.get_json()
        new_category = Catalog(data['name'])
        db_catalog.session.add(new_category)
        db_catalog.session.commit()
        return new_category.json(), 201

    def delete(self, id):
        category = Catalog.query.filter_by(id=id).first()
        if category:
            db_catalog.session.delete(category)
            db_catalog.session.commit()
            return {"Message": "Категория Удалена"}
        else:
            return {"Message": "Категория не найдена"}

    def put(self, id):
        data = request.get_json()
        category = Catalog.query.filter_by(id=id).first()
        if category:
            category.name = data["name"]
            db_catalog.session.add(category)
            db_catalog.session.commit()
            return {"Message": "Запись обновлена"}

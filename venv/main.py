from flask import Flask,request
import requests
from flask_restful import Api,Resource
from Models import catalog_model,podcatalog_model

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'a secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pod_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
app.config['RESTFUL_JSON'] = { 'ensure_ascii': False}
catalog_model.db_catalog.init_app(app)
podcatalog_model.db_podcatalog.init_app(app)


class Category(Resource):
    def get(self):
        catalog = catalog_model.Catalog.query.all()
        return  {"Category":list(x.json() for x in catalog )}

    def post(self):
        data = request.get_json()
        new_category = catalog_model.Catalog(data['name'])
        catalog_model.db_catalog.session.add(new_category)
        catalog_model.db_catalog.session.commit()
        return new_category.json(),201

    def delete(self, id):
        category = catalog_model.Catalog.query.filter_by(id=id).first()
        if category:
            catalog_model.db_catalog.session.delete(category)
            catalog_model.db_catalog.session.commit()
            return {"Message":"Категория Удалена"}
        else:
            return {"Message":"Категория не найдена"}

    def put (self,id):
        data = request.get_json()
        category = catalog_model.Catalog.query.filter_by(id=id).first()
        if category:
            category.name = data["name"]
            catalog_model.db_catalog.session.add(category)
            catalog_model.db_catalog.session.commit()
            return {"Message":"Запись обновлена"}

class Pod_category(Resource):
    def get(self,id):
        pod_catalog = podcatalog_model.Podcatalog.query.filter_by(id_catalog=id).all()
        return {"Pod_category": list(x.json() for x in pod_catalog)}

api.add_resource(Category,"/api/catalog","/api/catalog/<int:id>")
api.add_resource(Pod_category,"/api/podcatalog/<int:id>")

api.init_app(app)
if __name__ == "__main__":
    app.run(debug=True,port=5090,host="127.0.0.1")


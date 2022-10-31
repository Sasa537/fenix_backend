from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from fenix_site.Models.catalog_model import db_catalog
from fenix_site.Models.subcatalog_model import db_subcatalog
from fenix_site.Api.category_list_api import Category
from fenix_site.Api.subcategory import Subcategory

app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SECRET_KEY'] = 'a secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pod_catalog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['JSON_AS_ASCII'] = False
app.config['RESTFUL_JSON'] = {'ensure_ascii': False}
db_catalog.init_app(app)
db_subcatalog.init_app(app)


api.add_resource(Category, "/api/catalog/", "/api/catalog/<int:id>")
api.add_resource(Subcategory, "/api/subcatalog/", "/api/subcatalog/<int:id>")

if __name__ == "__main__":
    app.run(debug=True, port=5090, host="127.0.0.1")
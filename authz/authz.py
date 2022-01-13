from flask import Flask, Blueprint
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy # 17-1 : 32'
from flask_migrate import Migrate       # 17-1 : 32'
 
from authz.config import Config

db = SQLAlchemy() # 17-1 : 33'
mg = Migrate()    # 17-1 : 33'

apiv1_bp = Blueprint("apiv1_bp", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

from authz import resource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)      # 17-1 : 34'
    mg.init_app(app, db)  # 17-1 : 34'
    app.register_blueprint(apiv1_bp)
    return app

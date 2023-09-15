import os
from flask import Flask
from flask_migrate import Migrate

from config import config_settings
from app.models import db
from app.models import buddy,services,client,elder,service_request
from app.schema import ma


migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_settings[os.getenv('ENV')])

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    
    from app.routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


    return app

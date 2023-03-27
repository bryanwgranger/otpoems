import os
import requests
import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


db = SQLAlchemy()
migrate = Migrate()
def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from otpoems.main import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app

from otpoems import models
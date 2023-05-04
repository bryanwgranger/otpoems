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
    print(app.config.keys())
    #this_app.config.update({'SQL_DATABASE_URI' = 'testtesttest'})

    print('db before')
    db.init_app(app)
    print('db after')
    migrate.init_app(app, db)

    from app.main import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app

from app import models
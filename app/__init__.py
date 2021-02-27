from flask import Flask
from app.blueprints import Blueprints
from .extensions import db, migrate, marshmallow


def init_app():
    app = Flask(__name__)
    app.config.from_object("settings.Config")

    with app.app_context():
        #  initialize extensions
        db.init_app(app)
        migrate.init_app(app, db)
        marshmallow.init_app(app)
        Blueprints.register(app)
        return app

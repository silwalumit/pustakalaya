from flask import Flask
# from core import logger
from .extensions import db, migrate, marshmallow


def init_app():
    app = Flask(__name__)
    app.config.from_object("settings.Config")

    with app.app_context():

        #  initialize extensions
        db.init_app(app)
        migrate.init_app(app, db)
        from core import error_handlers
        from app.blueprints import Blueprints
        marshmallow.init_app(app)
        Blueprints.register(app)

        return app

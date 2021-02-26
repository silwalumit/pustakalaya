from flask import Flask
from flask_migrate import Migrate
from .auth.blueprints import Blueprints
from .extensions import db


def init_app():
    app = Flask(__name__)
    app.config.from_object("settings.Config")

    with app.app_context():
        #  extensions
        db.init_app(app)
        Migrate(app, db)
        Blueprints.register(app)
        return app

from logging import getLogger
from logging.config import dictConfig
from flask import Flask
from core.logger import Logger
from .extensions import db, migrate, marshmallow

dictConfig(Logger.get_config())
access_logger = getLogger('app.access')
err_logger = getLogger('app.error')


def init_app():
    app = Flask(__name__)
    app.config.from_object("settings.Config")

    with app.app_context():
        #  initialize extensions
        db.init_app(app)
        migrate.init_app(app, db)
        from core import error_handlers
        from app.blueprints import blueprints
        marshmallow.init_app(app)
        blueprints.init_app(app)
        return app

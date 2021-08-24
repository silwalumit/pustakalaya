from app.auth.routes import auth_bp


class Blueprints:
    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.register_blueprint(auth_bp, url_prefix='/auth')


blueprints = Blueprints()

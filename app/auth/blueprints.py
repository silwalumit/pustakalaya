from app.auth.routes import auth_bp


class Blueprints:
    @staticmethod
    def register(app):
        app.register_blueprint(auth_bp, url_prefix='/auth')
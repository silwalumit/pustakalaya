from flask import Blueprint
from flask_restful import Api
from app.auth.resources import LoginView, RegisterView

auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)

api.add_resource(LoginView, '/login')
api.add_resource(RegisterView, '/register')

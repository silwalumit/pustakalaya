from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash

from app.auth.serializers import UserRegisterSerializer
from core.exceptions import ValidationException


class LoginView(Resource):
    def post(self):
        pass


class RegisterView(Resource):

    @classmethod
    def post(cls):
        try:
            data = UserRegisterSerializer().load(request.json)
            # TODO validate user against existing user
            data.password = generate_password_hash(data.password)
            data.save()

        except ValidationError as err:
            raise ValidationException(err.messages)

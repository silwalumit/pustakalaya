from marshmallow import fields, validate, validates_schema, ValidationError, RAISE

from app.auth.models import User
from core.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User


class UserRegisterSerializer(ModelSerializer):
    username_regex = r'((?=^[a-zA-Z_])(?=\w*\d*)\w*)'
    name_regex = r'[a-zA-Z]+'
    password_regex = r'(?=.*\d+)(?=.*[#$@&_]+)(?=.*[A-Z]+)(?=.*[a-z]+)[a-zA-Z0-9_#$&@]'

    username = fields.String(
        required=True,
        validate=[
            validate.Regexp(username_regex, error="Invalid username!"),
            validate.Length(min=6, max=20, error="User name must be at least 6 and at most 20 character!")
        ]
    )
    first_name = fields.String(
        required=True,
        validate=[
            validate.Regexp(name_regex, error="Invalid first name!"),
            validate.Length(min=3, max=15)
        ]
    )

    last_name = fields.String(
        required=True,
        validate=[
            validate.Regexp(name_regex, error="Invalid last name!"),
            validate.Length(min=3, max=15)
        ]
    )
    email = fields.String(required=True, validate=validate.Email())
    password = fields.String(required=True, validate=validate.Regexp(password_regex))

    class Meta:
        model = User
        unknown = RAISE
        load_instance = True
        # fields = ('username', 'first_name', 'last_name', 'password', 'email','c_password')

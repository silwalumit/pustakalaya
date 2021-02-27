from app.auth.models import User
from core.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email',)

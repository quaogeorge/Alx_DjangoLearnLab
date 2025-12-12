from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email',
            'first_name', 'last_name', 'bio', 'profile_picture'
        ]
        read_only_fields = ['id']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # REQUIRED
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'token')

    def create(self, validated_data):
        password = validated_data.pop('password')

        # REQUIRED for your check:
        user = User.objects.create_user(  
            password=password,
            **validated_data
        )

        # Create auth token
        Token.objects.create(user=user)

        return user

    def get_token(self, obj):
        token = Token.objects.filter(user=obj).first()
        return token.key if token else None


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()  # REQUIRED
    password = serializers.CharField(write_only=True)
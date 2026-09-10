from rest_framework import serializers
from .models import CustomUSer
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    id = serializers.CharField(read_only = True)
    conf_password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUSer
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'address', 'password', 'conf_password']

    def validate(self, attrs):
        password = attrs.get('password')
        conf_password = attrs.get('conf_password')
        if password and conf_password and password != conf_password:
            raise ValidationError(detail='Parollar mos emas!')
        return attrs

    def create(self, validated_data):
        validated_data.pop("conf_password")
        return CustomUSer.objects.create_user(**validated_data)


    def to_representation(self, instance):
        user = super().to_representation(instance)
        return {
            "msg" : "Signed Up",
            "user" : user
        }



class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    token = serializers.CharField(read_only=True)
    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(
            username=username,
            password=password
        )
        if not user:
            raise ValidationError("Login yoki parol xato!")
        token, created = Token.objects.get_or_create(user=user)
        data["token"] = token.key
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUSer
        fields = ['id', 'first_name', 'last_name','username', 'email', 'address', 'phone_number']


class ProfileUpdateSerializer(ProfileSerializer):
    pass


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    conf_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        new_password = attrs.get("new_password")
        conf_password = attrs.get("conf_password")

        if new_password != conf_password:
            raise ValidationError(detail="Yangi parollar mos emas!")

        return attrs

    def update(self, instance, validated_data):
        old_password = validated_data['old_password']
        new_password = validated_data['new_password']
        if not instance.chech_password(old_password):
            raise ValidationError(detail="Eski parol xato!")
        instance.set_password(new_password)
        instance.save()
        return instance
        

        



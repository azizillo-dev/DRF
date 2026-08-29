from rest_framework import serializers
from .models import CustomUSer
from rest_framework.exceptions import ValidationError



class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    id = serializers.CharField(read_only = True)
    conf_password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUSer
        fields = ['id', 'first_name', 'last_name', 'email', 'address', 'password', 'conf_password']

    def validate(self, attrs):
        password = attrs.get('password')
        conf_password = attrs.get('conf_password')
        if password and conf_password and password != conf_password:
            raise ValidationError(detail='Parollar mos emas!')
        return attrs

    
from dataclasses import field
from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_username(self, data):
        if User.objects.filter(username=data).exists():
            raise ValidationError("Bu username band")
        return data

    







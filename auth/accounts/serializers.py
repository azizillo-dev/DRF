from rest_framework import serializers
from .models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'username', 'phone_number', 'address', 'password']

        def create(self, validated_data):
            password = validated_data.pop('password')

            user = CustomUser.objects.create_user(
                password=password,
                **validated_data
            )

            return user

        




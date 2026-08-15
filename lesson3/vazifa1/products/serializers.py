from rest_framework import serializers
from .models import Product
from rest_framework.exceptions import ValidationError



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



    def validate_description(self, data):
        if len(data) < 10:
            raise ValidationError("Description juda qisqa!")
        return data











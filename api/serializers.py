from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price']


class ProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title']

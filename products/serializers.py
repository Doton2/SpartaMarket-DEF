from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'content', 'image','author']

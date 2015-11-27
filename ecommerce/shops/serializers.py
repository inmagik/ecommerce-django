from rest_framework import serializers
from .models import Shop, Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        


class ShopSerializer(serializers.ModelSerializer):
    product_categories = ProductCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Shop

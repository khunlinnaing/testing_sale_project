from rest_framework import serializers
from .models import Category, Product, Orders

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'user']
        read_only_fields = ['user']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'amount', 'price', 'productimage', 'user']
        read_only_fields = ['user']


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'category', 'user', 'product', 'order_no', 'quantity', 'price', 'status']
        read_only_fields = ['user']
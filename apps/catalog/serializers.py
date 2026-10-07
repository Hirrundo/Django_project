from rest_framework import serializers
from .models import Category, Dish

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'is_active']
        read_only_fields = ['id']

class DishSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Dish
        fields = [

            'id', 'name', 'slug', 'description', 'price',
            'image', 'is_available', 'created_at',
            'category', 'category_name',
            ]
        read_only_fields = ['id', 'created_at', 'slug']
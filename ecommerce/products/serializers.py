from rest_framework import serializers
from .models import Product, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Category.objects.all(), source='category', required=False)

    class Meta:
        model = Product
        fields = ['id','name','sku','description','price','stock','is_active','category','category_id','seller','created_at','updated_at']
        read_only_fields = ['id','created_at','updated_at','seller']

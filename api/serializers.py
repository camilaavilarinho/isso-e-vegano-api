from rest_framework import serializers
from api.models import Category, Product

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #categories = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = ('url', 'name', 'image', 'categories')

from rest_framework import serializers
from .models import Item, Category

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['pk', 'name', 'price', 'description', 'published', 'deleted', 'categories']



class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'



class CategorySerializer(serializers.Serializer):


    class Meta:

        model = Category
        fields = ['name']


from rest_framework import serializers
from .models import Item, Category

class ItemSerializer(serializers.Serializer):

    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    price = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    published = serializers.BooleanField()
    deleted = serializers.BooleanField()

    class Meta:
        model = Item
        fields = ['name', 'price', 'description', 'published', 'deleted', 'categories']

    def create(self, validated_data):
        return Item.objects.create(**validated_data)


class CategorySerializer(serializers.Serializer):

    name = serializers.CharField()

    class Meta:

        model = Category
        fields = ['name']
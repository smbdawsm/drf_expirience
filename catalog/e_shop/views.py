from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework import generics, request

from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer, ItemDeleteSerializer



class ItemDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemDeleteView(generics.RetrieveUpdateAPIView):

    '''
    view for Удаление товаров (товар помечается как удаленный).
    изменяет параметр deleted для товара. оставляя его в базе.
    '''
    serializer_class = ItemDeleteSerializer
    queryset = Item.objects.all()

    def get(self, request, *args, **kwargs):
        '''
        Переопределенная функция из RetriveUpdateAPIView
        '''
        instance = self.get_object()
        instance.deleted = True
        instance.save()
        return Response({"success": "success"})

class CategoryDeleteView(generics.RetrieveUpdateAPIView):

    '''
    view for Удаление категорий (вернуть ошибку если категория прикреплена к товару)
    изменяет параметр deleted для товара. оставляя его в базе.
    '''
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        '''
        Переопределенная функция из RetriveUpdateAPIView
        '''
        useless = True
        instance = self.get_object()
        print(instance.pk)
        all_items = Item.objects.all()
        print(all_items)
        for cat in all_items:
            for el in cat.categories.all():
                print(el.pk)
                if el.pk == instance.pk:
                    useless = False
                    return Response({"error": "category is applied to a one or a more Item"})
        if useless == True:
            instance.delete()
            instance.save()
            return Response({"success": "success"})

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ItemListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ItemDeletedListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.filter(deleted=False)

class ItemPublishedListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        pub = self.request.query_params.get('status', None)
        print(pub)
        if pub is not None and pub == 'yes':
            queryset = queryset.filter(published=True)
        elif pub is not None and pub == 'no':
            queryset = queryset.filter(published=False)
        return queryset

class ItemPriceListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        min = self.request.query_params.get('min', None)
        max = self.request.query_params.get('max', None)
        if min is not None and max is not None:
            queryset = queryset.filter(price__gte=min, price__lte=max)
        return queryset

class ItemNameListView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__startswith=name)
        return queryset

class ItemCategoriesListView(generics.ListAPIView):
    serializer_class = ItemSerializer
    '''
    categories/all?category=<id>
    '''
    def get_queryset(self):
        result = []
        queryset = Item.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None and category is int:
            queryset = queryset.filter(categories=category)
            return queryset
        elif category.isdigit() == False:
            for obj in queryset:
                for el in obj.categories.all():
                    if el.name.startswith(category):
                        result.append(obj)
            queryset = result
        return queryset

class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemSerializer

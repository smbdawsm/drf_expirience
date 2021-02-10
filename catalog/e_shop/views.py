from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework import generics, request

from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer



class ItemDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

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

class ItemCreateView(generics.CreateAPIView):
    serializer_class = ItemSerializer
'''



class ItemView(CreateAPIView):

    serializer_class = ItemSerializer

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response({"items": serializer.data})

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_item = get_object_or_404(Item.objects.all(), pk=pk)
        data = request.data.get('items')
        serializer = ItemSerializer(instance=saved_item, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()

        return Response(
            {
                "success": f"Item {item_saved.name} saved."
            }
        )

    def delete(self, request, pk):
        item = get_object_or_404(Item.objects.all(), pk=pk)
        item.delete()
        return Response({
            "message": "Item with id `{}` has been deleted.".format(pk)
        }, status=204)

class CategoryView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(items, many=True)
        return Response({"Categories": serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotDeleteItemsView(APIView):

    def get(self, request):

        items = Item.objects.filter(deleted=False)
        serializer = ItemSerializer(items, many=True)
        return Response({"Not delete Items": serializer.data})

class PublishedView(APIView):

    def get(self, request):

        items = Item.objects.filter(published=True)
        serializer = ItemSerializer(items, many=True)
        return Response({"Published Items": serializer.data})

class NotPublishedView(APIView):

    def get(self, request):

        items = Item.objects.filter(published=False)
        serializer = ItemSerializer(items, many=True)
        return Response({"Not published Items": serializer.data})

'''
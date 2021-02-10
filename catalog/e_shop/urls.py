from django.urls import path

from .views import (ItemListView, ItemCreateView, ItemDetailView, ItemDeletedListView, ItemPublishedListView,
                    ItemPriceListView)


app_name = 'Market'

urlpatterns = [
    path('items/create', ItemCreateView.as_view()),
    path('items/all', ItemListView.as_view()),
    path('items/not-deleted', ItemDeletedListView.as_view()),
    path('items/published', ItemPublishedListView.as_view()),
    path('items/price', ItemPriceListView.as_view()),
    path('items/detail/<int:pk>', ItemDetailView.as_view()),
]
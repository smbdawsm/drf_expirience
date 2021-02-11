from django.urls import path

from .views import (ItemListView, ItemCreateView, ItemDetailView, ItemDeletedListView, ItemPublishedListView,
                    ItemPriceListView, ItemCategoriesListView, CategoryListView, CategoryCreateView,
                    ItemDeleteView, CategoryDeleteView, ItemNameListView)


app_name = 'Market'

urlpatterns = [
    path('items/create', ItemCreateView.as_view()),
    path('items/all', ItemListView.as_view()),
    path('items/not-deleted', ItemDeletedListView.as_view()),
    path('items/published', ItemPublishedListView.as_view()),
    path('items/price', ItemPriceListView.as_view()),
    path('items/categories', ItemCategoriesListView.as_view()),
    path('items/detail/<int:pk>', ItemDetailView.as_view()),
    path('categories/all', CategoryListView.as_view()),
    path('categories/create', CategoryCreateView.as_view()),
    path('categories/delete/<int:pk>', CategoryDeleteView.as_view()),
    path('items/delete/<int:pk>', ItemDeleteView.as_view()),
    path('items/name', ItemNameListView.as_view()),
]
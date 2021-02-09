from django.urls import path

from .views import ItemView

app_name = 'Market'

urlpatterns = [
    path('items/', ItemView.as_view()),
]
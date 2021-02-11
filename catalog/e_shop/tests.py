from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import  CategoryListView, CategoryCreateView
from rest_framework import status


class ItemTestCase(TestCase):


    def test_creation(self):
        view = CategoryCreateView.as_view()
        view2 = CategoryListView.as_view()
        factory = APIRequestFactory()
        test_category = {
                            "name": "test"
                        }
        create_category = factory.post('/categories/create', test_category)
        response1 = view(create_category)
        request2 = factory.get('categories/all')
        response = view2(request2)
        print(response)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
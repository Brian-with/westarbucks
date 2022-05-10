from django.urls import path

from .views import ProductsView
"""
127.0.0.1:8000/product
"""

urlpatterns = [
    path("", ProductsView.as_view()),
]
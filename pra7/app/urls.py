from django.urls import path
from .views import index,showProducts

urlpatterns = [
    path('', index),
    path('products/', showProducts),
]
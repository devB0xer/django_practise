from django.urls import path
from .views import somePage, getInfo

urlpatterns = [
    path('', getInfo),
]
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def showProducts(request):
    return render(request, 'clothes/products.html', [
        'clothes': '1' , 
    ])
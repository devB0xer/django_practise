from django.shortcuts import render, HttpResponse
from .models import Book

# Create your views here.

def somePage(request):
    return HttpResponse('<h1>hi</h1>')

def getInfo(request):
    book = Book.objects.get(id = 1)
    return render(request, 'base.html', {
        'book': book,
    })

def getAuthor(request):
    bookAuthor = Book.objects.filter(author__name = "") #unfinished here!
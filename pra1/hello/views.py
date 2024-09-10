from django.shortcuts import render, HttpResponse

def getHello(request):
    return HttpResponse('<h1>Hello, world</h1>')

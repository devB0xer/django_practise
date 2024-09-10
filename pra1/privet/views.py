from django.shortcuts import render, HttpResponse

def getPrivet(request):
    return HttpResponse('<h1>Привет</h1>')

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def ok_view(request):
    return render(request, 'index.html')
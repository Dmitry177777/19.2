from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index (request):
    return render (request, 'catalog/index.html')

def contacts (request):
    return HttpResponse ("Контакты:")
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def landing_page(request):
    #return HttpResponse("Hello  world")
    return render(request, 'controlador/index.html')
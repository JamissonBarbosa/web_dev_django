from django.shortcuts import render
from  controlador.models import Prateleira
from django.http import HttpResponse


def landing_page(request):
    #return HttpResponse("Hello  world")
    data = {}
    data['Prateleira'] = Prateleira.objects.all()
    return render(request, 'controlador/index.html')
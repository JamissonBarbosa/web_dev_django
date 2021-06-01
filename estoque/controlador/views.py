from django.shortcuts import render, redirect
from django.http import HttpResponse

from  .forms import PrateleiraForm
from  .models import Prateleira



def landing_page(request):
    #return HttpResponse("Hello  world")
    data = {}
    data['prateleiras'] = Prateleira.objects.all()
    return render(request, 'controlador/index.html', data)

def exibir_form(request):
    form = PrateleiraForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('url_landing_page')
    
    return render(request, 'controlador/form.html', {'form': form})


def update(request, pk):
    trans = Prateleira.objects.get(pk=pk)
    form =  PrateleiraForm(request.POST or None, instance=trans)
    
    if form.is_valid():
        form.save()
        return redirect('url_landing_page')
    
    return render(request, 'controlador/form.html', {'form': form})
    

def  delete(request, pk):
    trans = Prateleira.objects.get(pk=pk)
    trans.delete()
    return redirect('url_landing_page')
    
    
    
    
    
'''
data = "{"}
    data['prateleiras'] = Prateleira.objects.all() 
    
é igual a {'data': data}
'''
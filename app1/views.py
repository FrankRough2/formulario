from django.shortcuts import render
from .forms import FormularioForm
# Create your views here.

def add_formulario(request):
    if request.method == 'POST':
        form  = FormularioForm(request.POST)
        if form.is_valid():
            Formulario_item = form.save(commit=False)
            Formulario_item.save()
    else:
        form = FormularioForm()
    return render (request,'app1/formulario.html',{'form':form})

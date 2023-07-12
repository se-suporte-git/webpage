from django.shortcuts import render
from .models import Empresa
from django.shortcuts import render

def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'esg/lista_empresas.html', {'empresas': empresas})

def login(request):
    return render(request, 'esg/login.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Cliente, Proyecto



def index(request):
 return HttpResponse("Hello, world!")

class ProyectosListView(ListView):
    model = Proyecto
    template_name = 'Proyectos_detail.html'
    context_object_name = 'proyectos'

class ClienteListView(ListView):
    model = Cliente
    template_name = 'Cliente_detail.html'  # nombre del template que vas a usar
    context_object_name = 'clientes'

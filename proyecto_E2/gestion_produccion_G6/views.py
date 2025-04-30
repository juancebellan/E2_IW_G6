from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Cliente, Proyecto



def landing(request):
    return render(request, 'landing.html')

class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'proyecto_list.html'
    context_object_name = 'proyectos'

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'

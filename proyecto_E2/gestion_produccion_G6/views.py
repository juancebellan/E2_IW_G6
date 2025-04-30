from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Cliente, Empleado, Proyecto, Tarea



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

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado_list.html'
    context_object_name = 'empleados'
    
class TareaListView(ListView):
    model = Tarea
    template_name = 'tarea_list.html'
    context_object_name = 'tareas'

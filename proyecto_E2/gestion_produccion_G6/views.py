from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Empleado, Proyecto, Tarea
from django.urls import reverse_lazy


def landing(request):
    return render(request, 'landing.html')

# PROYECTO
class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'proyecto_list.html'
    context_object_name = 'proyectos'

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = 'proyecto_detail.html'

class ProyectoCreateView(CreateView):
    model = Proyecto
    fields = '__all__'
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    fields = '__all__'
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = 'proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')


# CLIENTE
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')
    context_object_name = "mi_cliente"

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = "mi_cliente"

class ClienteDeleteView(DeleteView):
    model = Proyecto
    template_name = 'cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente_list')
    context_object_name = "mi_cliente"



# EMPLEADO
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado_list.html'
    context_object_name = 'empleados'
    

# TAREA
class TareaListView(ListView):
    model = Tarea
    template_name = 'tarea_list.html'
    context_object_name = 'tareas'


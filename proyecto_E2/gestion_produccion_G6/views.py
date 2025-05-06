from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Empleado, Proyecto, Tarea
from django.urls import reverse, reverse_lazy


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
    context_object_name = 'proyecto'

class ProyectoCreateView(CreateView):
    model = Proyecto
    fields = '__all__'
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    fields = '__all__'
    template_name = 'proyecto_form.html'
    context_object_name = 'proyecto'
    def get_success_url(self):
        return reverse('proyecto_detail', kwargs={'pk': self.object.pk})

class ProyectoDeleteView(DeleteView):
    model = Proyecto
    template_name = 'proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')
    context_object_name = 'proyecto'


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

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente_form.html'
    context_object_name = 'cliente'
    def get_success_url(self):
        return reverse('cliente_detail', kwargs={'pk': self.object.pk})

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = "cliente"

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('cliente_list')



# EMPLEADO
class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleado_list.html'
    context_object_name = 'empleados'
    
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado_detail.html'
    context_object_name = 'empleado'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectos_como_responsable'] = self.object.proyectos_responsables.all()
        return context

class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleado_form.html'
    context_object_name = 'empleado'
    def get_success_url(self):
        return reverse('empleado_detail', kwargs={'pk': self.object.pk})

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')
    context_object_name = 'empleado'

    
# TAREA
class TareaListView(ListView):
    model = Tarea
    template_name = 'tarea_list.html'
    context_object_name = 'tareas'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha_actual'] = date.today()
        return context
class TareaDetailView(DetailView):
    model = Tarea
    template_name = 'tarea_detail.html'
    context_object_name = 'tarea'

class TareaCreateView(CreateView):
    model = Tarea
    fields = '__all__'
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tarea_list')

class TareaUpdateView(UpdateView):
    model = Tarea
    fields = '__all__'
    template_name = 'tarea_form.html'
    context_object_name = "tarea"
    def get_success_url(self):
        return reverse('tarea_detail', kwargs={'pk': self.object.pk})

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tarea_confirm_delete.html'
    context_object_name = "tarea"
    success_url = reverse_lazy('tarea_list')
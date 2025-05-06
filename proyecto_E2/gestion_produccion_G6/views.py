"""
Vistas para la aplicación de gestión de proyectos.
Contiene vistas para clientes, empleados, proyectos y tareas.
"""

from datetime import date
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Empleado, Proyecto, Tarea
from django.urls import reverse, reverse_lazy


def landing(request):
    """Vista para la página de inicio del sistema."""
    return render(request, 'landing.html')


# PROYECTO
class ProyectoListView(ListView):
    """Vista que muestra un listado de todos los proyectos."""
    model = Proyecto
    template_name = 'proyecto_list.html'
    context_object_name = 'proyectos'

class ProyectoDetailView(DetailView):
    """Vista que muestra el detalle de un proyecto específico."""
    model = Proyecto
    template_name = 'proyecto_detail.html'
    context_object_name = 'proyecto'

class ProyectoCreateView(CreateView):
    """Vista que permite crear un nuevo proyecto."""
    model = Proyecto
    fields = '__all__'
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

class ProyectoUpdateView(UpdateView):
    """Vista que permite editar un proyecto existente."""
    model = Proyecto
    fields = '__all__'
    template_name = 'proyecto_form.html'
    context_object_name = 'proyecto'

    def get_success_url(self):
        """Redirige al proyecto que se ha actualizado."""
        return reverse('proyecto_detail', kwargs={'pk': self.object.pk})

class ProyectoDeleteView(DeleteView):
    """Vista que permite eliminar un proyecto."""
    model = Proyecto
    template_name = 'proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')
    context_object_name = 'proyecto'


# CLIENTE
class ClienteListView(ListView):
    """Vista que muestra un listado de todos los clientes."""
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    """Vista que muestra el detalle de un cliente específico."""
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = "cliente"

class ClienteCreateView(CreateView):
    """Vista que permite crear un nuevo cliente."""
    model = Cliente
    fields = '__all__'
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')

class ClienteUpdateView(UpdateView):
    """Vista que permite editar un cliente existente."""
    model = Cliente
    fields = '__all__'
    template_name = 'cliente_form.html'
    context_object_name = 'cliente'

    def get_success_url(self):
        """Redirige al cliente que se ha actualizado."""
        return reverse('cliente_detail', kwargs={'pk': self.object.pk})

class ClienteDeleteView(DeleteView):
    """Vista que permite eliminar un cliente."""
    model = Cliente
    template_name = 'cliente_confirm_delete.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('cliente_list')


# EMPLEADO
class EmpleadoListView(ListView):
    """Vista que muestra un listado de todos los empleados."""
    model = Empleado
    template_name = 'empleado_list.html'
    context_object_name = 'empleados'

class EmpleadoDetailView(DetailView):
    """Vista que muestra el detalle de un empleado específico."""
    model = Empleado
    template_name = 'empleado_detail.html'
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        """Recupera todos proyectos donde el empleado es responsable."""
        context = super().get_context_data(**kwargs)
        context['proyectos_como_responsable'] = self.object.proyectos_responsables.all()
        return context

class EmpleadoCreateView(CreateView):
    """Vista que permite crear un nuevo empleado."""
    model = Empleado
    fields = '__all__'
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleado_list')

class EmpleadoUpdateView(UpdateView):
    """Vista que permite editar un empleado existente."""
    model = Empleado
    fields = '__all__'
    template_name = 'empleado_form.html'
    context_object_name = 'empleado'

    def get_success_url(self):
        """Redirige al empleado que se ha actualizado."""
        return reverse('empleado_detail', kwargs={'pk': self.object.pk})

class EmpleadoDeleteView(DeleteView):
    """Vista que permite eliminar un empleado."""
    model = Empleado
    template_name = 'empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')
    context_object_name = 'empleado'


# TAREA
class TareaListView(ListView):
    """Vista que muestra un listado de todas las tareas."""
    model = Tarea
    template_name = 'tarea_list.html'
    context_object_name = 'tareas'

    def get_context_data(self, **kwargs):
        """Se usa para obtener la fecha actual para despues comparar con la fecha de las tareas."""
        context = super().get_context_data(**kwargs)
        context['fecha_actual'] = date.today()
        return context

class TareaDetailView(DetailView):
    """Vista que muestra el detalle de una tarea específica."""
    model = Tarea
    template_name = 'tarea_detail.html'
    context_object_name = 'tarea'

class TareaCreateView(CreateView):
    """Vista que permite crear una nueva tarea."""
    model = Tarea
    fields = '__all__'
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tarea_list')

class TareaUpdateView(UpdateView):
    """Vista que permite editar una tarea existente."""
    model = Tarea
    fields = '__all__'
    template_name = 'tarea_form.html'
    context_object_name = "tarea"

    def get_success_url(self):
        """Redirige a la tarea que se ha actualizado."""
        return reverse('tarea_detail', kwargs={'pk': self.object.pk})

class TareaDeleteView(DeleteView):
    """Vista que permite eliminar una tarea."""
    model = Tarea
    template_name = 'tarea_confirm_delete.html'
    context_object_name = "tarea"
    success_url = reverse_lazy('tarea_list')

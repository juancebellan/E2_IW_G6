"""
Vistas para la aplicación de gestión de proyectos.
Contiene vistas para clientes, empleados, proyectos y tareas.
"""

from datetime import date
import re
from urllib import request
from urllib.parse import urlparse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Empleado, Proyecto, Tarea
from django.urls import path, reverse, reverse_lazy
from .forms import ProyectoForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

def if_detail(request,context):
        volver = request.META.get('HTTP_REFERER')
        if volver:
            path = urlparse(volver).path
            if re.match(r".*/\d+/?$", path):
                context['volver'] = volver
        return context

def landing(request):
    """Vista para la página de inicio del sistema."""
    return render(request, 'landing.html')


# PROYECTO
class ProyectoListView(ListView):
    """Vista que muestra un listado de todos los proyectos."""
    model = Proyecto
    template_name = 'proyecto_list.html'
    context_object_name = 'proyectos'

    def get(self, request, *args, **kwargs):
        vengo_de = request.GET.get('vengo_de', None)
        if vengo_de == "boton_arriba":
            request.session['origen'] = request.build_absolute_uri()
        return super().get(request, *args, **kwargs)


class ProyectoDetailView(DetailView):
    """Vista que muestra el detalle de un proyecto específico."""
    model = Proyecto
    template_name = 'proyecto_detail.html'
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyecto_cliente'] = self.object.cliente
        context = if_detail(self.request, context)
        context['origen']=self.request.session.get('origen',None)
        return context


class ProyectoCreateView(CreateView):
    """Vista que permite crear un nuevo proyecto."""
    model = Proyecto
    form_class = ProyectoForm  
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        return context


class ProyectoUpdateView(UpdateView):
    """Vista que permite editar un proyecto existente."""
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'
    context_object_name = 'proyecto'
    ordering = ['nombre']
    
    def get_success_url(self):
        """Redirige al proyecto que se ha actualizado."""

        return reverse('proyecto_detail', kwargs={'pk': self.object.pk})


class ProyectoDeleteView(DeleteView):
    """Vista que permite eliminar un proyecto."""
    model = Proyecto
    template_name = 'proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request,context)
        return context



# CLIENTE
class ClienteListView(ListView):
    """Vista que muestra un listado de todos los clientes."""
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        context['origen']=self.request.session.get('origen',None)
        return context


class ClienteDetailView(DetailView):
    """Vista que muestra el detalle de un cliente específico."""
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = "cliente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        context['origen']=self.request.session.get('origen',None)
        return context
    

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        return context



# EMPLEADO
class EmpleadoListView(ListView):
    """Vista que muestra un listado de todos los empleados."""
    model = Empleado
    template_name = 'empleado_list.html'
    context_object_name = 'empleados'
    ordering = ['nombre']

    def get(self, request, *args, **kwargs):
        vengo_de = request.GET.get('vengo_de', None)
        if vengo_de == "boton_arriba":
            request.session['origen'] = request.build_absolute_uri()
        return super().get(request, *args, **kwargs)


class EmpleadoDetailView(DetailView):
    """Vista que muestra el detalle de un empleado específico."""
    model = Empleado
    template_name = 'empleado_detail.html'
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        """Recupera todos proyectos donde el empleado es responsable."""
        context = super().get_context_data(**kwargs)
        context['proyectos_como_responsable'] = self.object.proyectos_responsables.all()
        context = if_detail(self.request, context)
        context['origen']=self.request.session.get('origen',None)
        return context
    
    
class EmpleadoCreateView(CreateView):
    """Vista que permite crear un nuevo empleado."""
    model = Empleado
    fields = '__all__'
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleado_list')

    def form_valid(self, form):
        response = super().form_valid(form) 
        empleado = self.object   

        mensaje = f"""
        ¡Hola {empleado.nombre} {empleado.apellidos}!

        En nombre de todo el equipo de Deustotil S.L, quiero darte una calurosa bienvenida. Estamos muy emocionados de que te unas a nosotros y confiamos en que tu talento y 
        dedicación serán una gran adición a nuestra familia.

        Aquí en Deustotil, valoramos el trabajo en equipo, la innovación y la pasión por lo que hacemos. Creemos que juntos alcanzaremos grandes logros, y estamos seguros de que te
        sentirás como en casa en poco tiempo.

        A lo largo de tu proceso de integración, tendrás el apoyo de todo el equipo para que tu transición sea lo más fluida posible. Si en algún momento tienes preguntas o necesitas
        algo, no dudes en acercarte a cualquiera de nosotros.

        ¡Esperamos que disfrutes de esta nueva etapa y que juntos podamos construir un futuro brillante!

        Bienvenido nuevamente, ¡estamos felices de tenerte con nosotros!

        Saludos cordiales,  
        Deustotil S.L
        """
           

        # send_mail(
        #     subject="Bienvenido al grupo Deustotil S.L!!",
        #     message= mensaje,
        #     from_email="infotareasg6@gmail.com",
        #     recipient_list=[empleado.email], 
        #     fail_silently=False,
            
        # )

        return response
        

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        return context



# TAREA
class TareaListView(ListView):
    """Vista que muestra un listado de todas las tareas."""
    model = Tarea
    template_name = 'tarea_list.html'
    context_object_name = 'tareas'

    def get(self, request, *args, **kwargs):
        vengo_de = request.GET.get('vengo_de', None)
        if vengo_de == "boton_arriba":
            request.session['origen'] = request.build_absolute_uri()
        return super().get(request, *args, **kwargs)

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        return context
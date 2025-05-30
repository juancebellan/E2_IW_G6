"""
Vistas para la aplicación de gestión de proyectos.
Contiene vistas para clientes, empleados, proyectos y tareas.
"""

from datetime import date
import re
from urllib import request
from urllib.parse import urlparse
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cliente, Empleado, Proyecto, Tarea
from django.urls import path, reverse, reverse_lazy
from .forms import ProyectoForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProyectoForm, RegistroForm, EmpleadoForm


def if_detail(request, context):
    """Agrega al contexto la URL de la que proviene la petición si corresponde a un detalle (con ID numérico al final)."""
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
class ProyectoListView(LoginRequiredMixin, ListView):
    """Vista que muestra un listado de todos los proyectos."""
    model = Proyecto
    template_name = 'proyecto_list.html'
    context_object_name = 'proyectos'

    def get(self, request, *args, **kwargs):
        vengo_de = request.GET.get('vengo_de', None)
        if vengo_de == "boton_arriba":
            request.session['origen'] = request.build_absolute_uri()
        return super().get(request, *args, **kwargs)


class ProyectoDetailView(LoginRequiredMixin, DetailView):
    """Vista que muestra el detalle de un proyecto específico."""
    model = Proyecto
    template_name = 'proyecto_detail.html'
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        context['origen'] = self.request.session.get('origen', None)
        return context


class ProyectoCreateView(LoginRequiredMixin, CreateView):
    """Vista que permite crear un nuevo proyecto."""
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        return context


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    """Vista que permite editar un proyecto existente."""
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyecto_form.html'
    context_object_name = 'proyecto'
    ordering = ['nombre']

    def get_success_url(self):
        """Redirige al proyecto que se ha actualizado."""
        return reverse('proyecto_detail', kwargs={'pk': self.object.pk})


class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    """Vista que permite eliminar un proyecto."""
    model = Proyecto
    template_name = 'proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')
    context_object_name = 'proyecto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        return context


# CLIENTE
class ClienteListView(LoginRequiredMixin, ListView):
    """Vista que muestra un listado de todos los clientes."""
    model = Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        context['origen'] = self.request.session.get('origen', None)
        return context


class ClienteDetailView(LoginRequiredMixin, DetailView):
    """Vista que muestra el detalle de un cliente específico."""
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = "cliente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectos'] = self.object.proyectos.all()
        context = if_detail(self.request, context)
        context['origen'] = self.request.session.get('origen', None)
        return context


class ClienteCreateView(LoginRequiredMixin, CreateView):
    """Vista que permite crear un nuevo cliente."""
    model = Cliente
    fields = '__all__'
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('cliente_list')


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    """Vista que permite editar un cliente existente."""
    model = Cliente
    fields = '__all__'
    template_name = 'cliente_form.html'
    context_object_name = 'cliente'

    def get_success_url(self):
        """Redirige al cliente que se ha actualizado."""
        return reverse('cliente_detail', kwargs={'pk': self.object.pk})


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
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
class EmpleadoListView(LoginRequiredMixin, ListView):
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


class EmpleadoDetailView(LoginRequiredMixin, DetailView):
    """Vista que muestra el detalle de un empleado específico."""
    model = Empleado
    template_name = 'empleado_detail.html'
    context_object_name = 'empleado'

    def get_context_data(self, **kwargs):
        """Recupera todos proyectos donde el empleado es responsable."""
        context = super().get_context_data(**kwargs)
        context['proyectos_como_responsable'] = self.object.proyectos_responsables.all()
        context = if_detail(self.request, context)
        context['origen'] = self.request.session.get('origen', None)
        return context


class EmpleadoCreateView(LoginRequiredMixin, CreateView):
    """Vista que permite crear un nuevo empleado."""
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    success_url = reverse_lazy('empleado_list')

    def form_valid(self, form):
        """Envía un correo de bienvenida al nuevo empleado."""
        response = super().form_valid(form)
        empleado = self.object

        mensaje = f"""
        ¡Buenas {empleado.nombre}!

        En nombre de todo el equipo de Deustotil Tech S.L, quiero darte una calurosa bienvenida. Estamos muy emocionados de que te unas a nosotros y confiamos en que tu talento y 
        dedicación serán una gran adición a nuestra familia.

        Aquí en Deustotil, valoramos el trabajo en equipo, la innovación y la pasión por lo que hacemos. Creemos que juntos alcanzaremos grandes logros, y estamos seguros de que te
        sentirás como en casa en poco tiempo.

        A lo largo de tu proceso de integración, tendrás el apoyo de todo el equipo para que tu transición sea lo más fluida posible. Si en algún momento tienes preguntas o necesitas
        algo, no dudes en acercarte a cualquiera de nosotros.

        ¡Esperamos que disfrutes de esta nueva etapa y que juntos podamos construir un futuro brillante!

        Bienvenido nuevamente, ¡estamos felices de tenerte con nosotros!

        Saludos cordiales,  
        Deustotil Tech S.L
        """

        send_mail(
            subject="Bienvenido al grupo Deustotil Tech S.L!!",
            message=mensaje,
            from_email="infotareasg6@gmail.com",
            recipient_list=[empleado.email],
            fail_silently=False,
        )

        return response


class EmpleadoUpdateView(LoginRequiredMixin, UpdateView):
    """Vista que permite editar un empleado existente."""
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado_form.html'
    context_object_name = 'empleado'

    def get_success_url(self):
        """Redirige al empleado que se ha actualizado."""
        return reverse('empleado_detail', kwargs={'pk': self.object.pk})


class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
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
class TareaListView(LoginRequiredMixin, ListView):
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


class TareaDetailView(LoginRequiredMixin, DetailView):
    """Vista que muestra el detalle de una tarea específica."""
    model = Tarea
    template_name = 'tarea_detail.html'
    context_object_name = 'tarea'


class TareaCreateView(LoginRequiredMixin, CreateView):
    """Vista que permite crear una nueva tarea."""
    model = Tarea
    fields = '__all__'
    template_name = 'tarea_form.html'
    success_url = reverse_lazy('tarea_list')


class TareaUpdateView(LoginRequiredMixin, UpdateView):
    """Vista que permite editar una tarea existente."""
    model = Tarea
    fields = '__all__'
    template_name = 'tarea_form.html'
    context_object_name = "tarea"

    def get_success_url(self):
        """Redirige a la tarea que se ha actualizado."""
        return reverse('tarea_detail', kwargs={'pk': self.object.pk})


class TareaDeleteView(LoginRequiredMixin, DeleteView):
    """Vista que permite eliminar una tarea."""
    model = Tarea
    template_name = 'tarea_confirm_delete.html'
    context_object_name = "tarea"
    success_url = reverse_lazy('tarea_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = if_detail(self.request, context)
        return context


# LOGIN
class RegistroView(CreateView):
    """Vista para registrar un nuevo usuario en el sistema."""
    form_class = RegistroForm
    template_name = 'registro.html'
    success_url = reverse_lazy('login')


# Obtener datos para JavaScript (AJAX)
def get_cliente(request, pk):
    """Devuelve información de un cliente (nacionalidad y proyectos) en formato JSON."""
    try:
        cliente = Cliente.objects.get(id=pk)
        proyectos = cliente.proyectos.all().values('nombre')
        data = {
            "Nacionalidad": cliente.nacionalidad,
            "proyectos": list(proyectos)
        }
        return JsonResponse(data, safe=False)
    except Cliente.DoesNotExist:
        raise Http404("Cliente no encontrado")


def get_empleados(request, pk):
    """Devuelve información de un empleado (DNI, proyectos y tareas) en formato JSON."""
    try:
        empleado = Empleado.objects.get(id=pk)
        proyectos = empleado.proyectos_responsables.all().values('nombre')
        tareas = empleado.tareas_empleado.all().values('nombre')
        data = {
            "Dni": empleado.dni,
            "Proyectos": list(proyectos),
            "Tareas": list(tareas)
        }
        return JsonResponse(data, safe=False)
    except Empleado.DoesNotExist:
        raise Http404("Empleado no encontrado")


def get_proyectos(request, pk):
    """Devuelve información de un proyecto (fecha fin, presupuesto, cliente, empleados) en formato JSON."""
    try:
        proyecto = Proyecto.objects.get(id=pk)
        presupuesto = f"{proyecto.presupuesto}€"
        nombres_empleados = [empleado.nombre for empleado in proyecto.responsables.all()]
        cliente = proyecto.cliente.nombre if proyecto.cliente else "No hay un cliente asociado"
        data = {
            "Fecha fin": proyecto.fecha_fin,
            "Presupuesto": presupuesto,
            "Cliente": cliente,
            "Empleados": nombres_empleados
        }
        return JsonResponse(data, safe=False)
    except Proyecto.DoesNotExist:
        raise Http404("Proyecto no encontrado")


def get_tareas(request, pk):
    """Devuelve información de una tarea (descripción, proyecto, fechas, prioridad, estado, notas) en formato JSON."""
    try:
        tarea = Tarea.objects.get(id=pk)
        data = {
            "Descripcion": tarea.descripcion,
            "Proyecto": tarea.proyecto.nombre,
            "Fecha fin": tarea.fecha_fin,
            "Prioridad": tarea.prioridad,
            "Estado": tarea.estado,
            "Notas": tarea.notas
        }
        return JsonResponse(data, safe=False)
    except Tarea.DoesNotExist:
        raise Http404("Tarea no encontrada")




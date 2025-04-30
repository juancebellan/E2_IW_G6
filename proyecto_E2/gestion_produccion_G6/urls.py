from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'), 
    path('tareas/', views.TareaListView.as_view(), name='tarea_list'), 
]

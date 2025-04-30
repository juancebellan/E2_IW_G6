from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto_detail'),
    path('proyectos/nuevo/', views.ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyectos/<int:pk>/editar/', views.ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyectos/<int:pk>/borrar/', views.ProyectoDeleteView.as_view(), name='proyecto_delete'),
    
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'), 
    path('tareas/', views.TareaListView.as_view(), name='tarea_list'), 
]

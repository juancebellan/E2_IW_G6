from django.urls import path

from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('proyectos', views.ProyectosListView.as_view(), name='ProyectosListView'),
 path('clientes', views.ClienteListView.as_view(), name='ClientesListView'),
]
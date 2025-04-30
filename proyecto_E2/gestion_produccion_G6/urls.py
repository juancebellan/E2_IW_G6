from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
]

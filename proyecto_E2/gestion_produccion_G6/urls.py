from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.landing, name='landing'),

    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('proyectos/<int:pk>/', views.ProyectoDetailView.as_view(), name='proyecto_detail'),
    path('proyectos/nuevo/', views.ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyectos/<int:pk>/editar/', views.ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyectos/<int:pk>/borrar/', views.ProyectoDeleteView.as_view(), name='proyecto_delete'),

    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:pk>/borrar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),

    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('empleados/nuevo/', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/editar/', views.EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/<int:pk>/borrar/', views.EmpleadoDeleteView.as_view(), name='empleado_delete'),

    path('tareas/', views.TareaListView.as_view(), name='tarea_list'),
    path('tareas/<int:pk>/', views.TareaDetailView.as_view(), name='tarea_detail'),
    path('tareas/nueva/', views.TareaCreateView.as_view(), name='tarea_create'),
    path('tareas/<int:pk>/editar/', views.TareaUpdateView.as_view(), name='tarea_update'),
    path('tareas/<int:pk>/borrar/', views.TareaDeleteView.as_view(), name='tarea_delete'),

    # APIS
    path('api/clientes/<int:pk>/', views.get_cliente, name='api_clientes'),
    path('api/empleados/<int:pk>/', views.get_empleados, name='api_empleado'),
    path('api/proyectos/<int:pk>/', views.get_proyectos, name='api_proyectos'),
    path('api/tareas/<int:pk>/', views.get_tareas, name='api_tareas'),

    # LOG-IN
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='login.html',  redirect_authenticated_user=True, next_page='landing'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
]

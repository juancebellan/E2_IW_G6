import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_E2.settings')
django.setup()

from gestion_produccion_G6.models import Empleado, Cliente, Proyecto, Tarea

# --- Empleados ---
empleados = [
    Empleado(dni="12345678Z", nombre="Carlos", apellidos="Lopez Garcia", email="carlos.lopez@example.com", telefono="600123456"),
    Empleado(dni="23456789X", nombre="Lucia", apellidos="Fernandez Perez", email="lucia.fernandez@example.com", telefono="600234567"),
    Empleado(dni="34567890M", nombre="David", apellidos="Martinez Ruiz", email="david.martinez@example.com", telefono="600345678"),
    Empleado(dni="45678901B", nombre="Ana", apellidos="Sanchez Torres", email="ana.sanchez@example.com", telefono="600456789"),
    Empleado(dni="56789012L", nombre="Jorge", apellidos="Ramirez Diaz", email="jorge.ramirez@example.com", telefono="600567890"),
    Empleado(dni="67890123K", nombre="Claudia", apellidos="Romero Soto", email="claudia.romero@example.com", telefono="600678901"),
    Empleado(dni="78901234S", nombre="Miguel", apellidos="Alonso Vera", email="miguel.alonso@example.com", telefono="600789012"),
    Empleado(dni="89012345H", nombre="Marta", apellidos="Moreno Vidal", email="marta.moreno@example.com", telefono="600890123"),
    Empleado(dni="90123456T", nombre="Sergio", apellidos="Gutierrez Lozano", email="sergio.gutierrez@example.com", telefono="600901234"),
    Empleado(dni="01234567R", nombre="Paula", apellidos="Cruz Navarro", email="paula.cruz@example.com", telefono="600012345"),
]
Empleado.objects.bulk_create(empleados)

# --- Clientes ---
clientes = [
    Cliente(cif="A12345678", nombre="Grupo Tech SA", nacionalidad="Espanola"),
    Cliente(cif="B23456789", nombre="Soluciones Digitales SL", nacionalidad="Espanola"),
    Cliente(cif="C34567890", nombre="Innovacion Global SL", nacionalidad="Argentina"),
    Cliente(cif="D45678901", nombre="Data Soft Ltd", nacionalidad="Colombiana"),
    Cliente(cif="E56789012", nombre="DevMasters Inc", nacionalidad="Mexicana"),
    Cliente(cif="F67890123", nombre="SoftWorks", nacionalidad="Espanola"),
    Cliente(cif="G78901234", nombre="Optima Tech", nacionalidad="Chilena"),
    Cliente(cif="H89012345", nombre="CiberProyectos SA", nacionalidad="Peruana"),
    Cliente(cif="I90123456", nombre="Consultores IT", nacionalidad="Espanola"),
    Cliente(cif="J01234567", nombre="RedVision SL", nacionalidad="Uruguaya"),
]
Cliente.objects.bulk_create(clientes)

# --- Proyectos ---
clientes_bd = list(Cliente.objects.all())
proyectos = [
    Proyecto(nombre="App Movil Ventas", descripcion="Aplicacion movil para ventas y reportes", fecha_ini=datetime.date(2025,1,10), fecha_fin=datetime.date(2025,5,20), presupuesto=15000, cliente=clientes_bd[0]),
    Proyecto(nombre="Sistema Contable", descripcion="Herramienta web para gestion contable", fecha_ini=datetime.date(2025,2,15), fecha_fin=datetime.date(2025,6,15), presupuesto=20000, cliente=clientes_bd[1]),
    Proyecto(nombre="Dashboard BI", descripcion="Dashboard de inteligencia empresarial", fecha_ini=datetime.date(2025,3,1), fecha_fin=datetime.date(2025,7,30), presupuesto=17000, cliente=clientes_bd[2]),
    Proyecto(nombre="Control Produccion", descripcion="Control y seguimiento de produccion", fecha_ini=datetime.date(2025,1,20), fecha_fin=datetime.date(2025,6,1), presupuesto=22000, cliente=clientes_bd[3]),
    Proyecto(nombre="Gestor de Tareas", descripcion="Sistema de tareas y productividad", fecha_ini=datetime.date(2025,4,1), fecha_fin=datetime.date(2025,8,15), presupuesto=13000, cliente=clientes_bd[4]),
    Proyecto(nombre="CRM Clientes", descripcion="Gestion de relaciones con clientes", fecha_ini=datetime.date(2025,5,10), fecha_fin=datetime.date(2025,9,10), presupuesto=25000, cliente=clientes_bd[5]),
    Proyecto(nombre="App Eventos", descripcion="Aplicacion para organizacion de eventos", fecha_ini=datetime.date(2025,2,5), fecha_fin=datetime.date(2025,6,30), presupuesto=14000, cliente=clientes_bd[6]),
    Proyecto(nombre="Portal de Empleo", descripcion="Plataforma de ofertas de trabajo", fecha_ini=datetime.date(2025,3,20), fecha_fin=datetime.date(2025,7,20), presupuesto=18000, cliente=clientes_bd[7]),
    Proyecto(nombre="Sistema Inventario", descripcion="Gestion de stock y almacenes", fecha_ini=datetime.date(2025,1,15), fecha_fin=datetime.date(2025,5,15), presupuesto=16000, cliente=clientes_bd[8]),
    Proyecto(nombre="Modulo Reportes", descripcion="Sistema para generacion de reportes PDF", fecha_ini=datetime.date(2025,4,25), fecha_fin=datetime.date(2025,9,25), presupuesto=12000, cliente=clientes_bd[9]),
]
Proyecto.objects.bulk_create(proyectos)

# ... (empleados, clientes y proyectos se crean con bulk_create igual)

# Obtener listas actualizadas de empleados y proyectos
empleados_bd = list(Empleado.objects.all())
proyectos_bd = list(Proyecto.objects.all())

# Crear tareas guardándolas una a una para asegurar integridad
for i in range(10):
    tarea = Tarea(
        proyecto=proyectos_bd[i],
        empleado=empleados_bd[i],
        nombre=f"Tarea {i+1}",
        descripcion="Descripcion de la tarea asignada",
        fecha_ini=datetime.date(2025, 5, 1),
        fecha_fin=datetime.date(2025, 6, 1),
        prioridad="Media",
        estado="Asignado",
        notas="Sin comentarios"
    )
    tarea.save()

print("Datos creados correctamente, incluyendo tareas.")

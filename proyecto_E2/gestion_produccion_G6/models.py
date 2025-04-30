import datetime
from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, default="Descripción no proporcionada")
    fecha_ini = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(default=datetime.date.today)
    presupuesto = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE) 
    cif = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default="Descripción de la tarea")
    fecha_ini = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(default=datetime.date.today)
    prioridad = models.CharField(
        max_length=20,
        choices=[
            ('Baja', 'Baja'), 
            ('Media', 'Media'), 
            ('Alta', 'Alta')],
        default='Baja'
    )    
    estado = models.CharField(
        max_length=20,
        choices=[
            ('Abierto', 'Abierto'),
            ('Asignado', 'Asignado'),
            ('En proceso', 'En proceso'),
            ('Finalizada', 'Finalizada')
        ],
        default='Abierto'
    )    
    notas = models.TextField(default="Notas del empleado")
    def __str__(self):
        return self.nombre

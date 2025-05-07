import datetime
from django.db import models
from django.forms import ValidationError


class Proyecto(models.Model):
    """
    Modelo que representa un proyecto de la empresa.

    Atributos:
        nombre: Nombre del proyecto.
        descripcion: Descripción del proyecto.
        fecha_ini: Fecha de inicio del proyecto.
        fecha_fin: Fecha estimada de finalización.
        presupuesto: Presupuesto asignado.
        responsables: Empleados asignados como responsables del proyecto.
    """
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500, default="Descripción no proporcionada")
    fecha_ini = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(default=datetime.date.today)
    presupuesto = models.IntegerField(default=0)
    responsables = models.ManyToManyField('Empleado', blank=True, related_name='proyectos_responsables')
    def __str__(self):
        """Devuelve el nombre del proyecto."""
        return self.nombre
    def clean(self):
        """
        Valida que la fecha de inicio sea anterior o igual a la fecha de fin.
        """
        if self.fecha_ini and self.fecha_fin and self.fecha_ini > self.fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin del proyecto.")


class Empleado(models.Model):
    """
    Modelo que representa un empleado de la empresa.

    Atributos:
        dni: DNI del empleado, es único.
        nombre: Nombre del empleado.
        apellidos: Apellidos del empleado.
        email: Correo electrónico.
        telefono: Número de teléfono.
    """
    dni = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    def __str__(self):
        """Devuelve el nombre del empleado."""
        return self.nombre


class Cliente(models.Model):
    """
    Modelo que representa un cliente que se encarga de un proyecto.

    Atributos:
        proyecto: Proyecto asociado al cliente.
        cif: Código de Identificación Fiscal, es único.
        nombre: Nombre del cliente o empresa.
        nacionalidad: Nacionalidad del cliente.
    """
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE) 
    cif = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    def __str__(self):
        """Devuelve el nombre del cliente."""
        return self.nombre


class Tarea(models.Model):
    """
    Modelo que representa una tarea asignada a un empleado dentro de un proyecto.

    Atributos:
        proyecto: Proyecto al que pertenece la tarea.
        empleado: Empleado responsable de realizarla.
        nombre: Título de la tarea.
        descripcion: Explicación detallada de la tarea.
        fecha_ini: Fecha de inicio de la tarea.
        fecha_fin: Fecha prevista de finalización.
        prioridad: Grado de prioridad asignado.
        estado: Estado actual de la tarea.
        notas: Comentarios o seguimiento adicional.
    """
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
        """Devuelve el nombre de la tarea"""
        return self.nombre
    def clean(self):
        """
        Valida que la fecha de inicio sea anterior o igual a la fecha de fin.
        """
        if self.fecha_ini and self.fecha_fin and self.fecha_ini > self.fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")

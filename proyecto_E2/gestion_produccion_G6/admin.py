from django.contrib import admin

from .models import Cliente, Empleado, Proyecto, Tarea
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Tarea)
admin.site.register(Proyecto)

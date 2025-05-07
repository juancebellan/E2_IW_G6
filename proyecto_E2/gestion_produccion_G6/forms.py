from django import forms
from .models import Proyecto, Empleado

class ProyectoForm(forms.ModelForm):
    """
    Formulario personalizado para el modelo Proyecto.
    Se utiliza un widget de checkbox múltiple para seleccionar los empleados responsables,
    en lugar del selector por defecto.
    """
    class Meta:
        model = Proyecto
        fields = '__all__'
        widgets = {
            'responsables': forms.CheckboxSelectMultiple()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['responsables'].queryset = Empleado.objects.order_by('nombre')

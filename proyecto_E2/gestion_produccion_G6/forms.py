from django import forms
from .models import Proyecto, Empleado
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email
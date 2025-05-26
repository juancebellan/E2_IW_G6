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
    """
    Formulario personalizado para el registro de nuevos usuarios.
    Añade el campo 'email' como obligatorio y valida que no se repita un correo ya registrado.
    Hereda de UserCreationForm, incluyendo los campos de nombre de usuario y contraseñas.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email
    

class EmpleadoForm(forms.ModelForm):
    """
    Formulario personalizado para el modelo Empleado.
    Se incluye una validación personalizada del campo DNI, tanto en el frontend (JS) como en el backend (Django),
    y se añade un identificador HTML al campo para permitir la validación en cliente.
    """

    class Meta:
        model = Empleado
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dni'].widget.attrs.update({'id': 'dni'})

    def clean_dni(self):
        dni = self.cleaned_data.get('dni', '').upper()
        import re
        if not re.match(r'^[0-9]{8}[A-Z]$', dni):
            raise forms.ValidationError("El DNI no tiene un formato válido. Debe tener 8 números y una letra mayúscula (ej: 12345678Z).")
        return dni

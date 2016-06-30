from django import forms
from models import Odontologo
from views import *
from django.contrib.auth.forms import AdminPasswordChangeForm


class OdontologoCreateForm(forms.ModelForm):
    """
    Clase que contiene los campos del formulario, necesarios para el registro de nuevos Odontologos
    en la base de datos.

    """
    nombre = forms.CharField(max_length=30, required=True, label='Nombre')
    especialidad = forms.CharField(max_length=30, required=True, label='Especialidad')
    email = forms.EmailField(required=True)
    telefono = forms.RegexField(regex=r'^[\d()+-]+$', max_length=20,
                                help_text='Digitos y + - ( ) solamente.')
    direccion = forms.CharField(max_length=50)

    class Meta:
        model = Odontologo
        fields = ['nombre', 'especialidad', 'email', 'telefono', 'direccion']

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("No se puede crear Odontologo")
        odontologo = super(OdontologoCreateForm, self).save(commit=True)
        odontologo.save()
        return odontologo



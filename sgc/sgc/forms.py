from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserProfileForm(forms.ModelForm):
    """
    Clase que contiene los campos del formulario, para la modificacion dle perfil del usuario registrado en la base de datos.
    """


    nombre = forms.CharField(max_length=30, required=True, label='Nombre')
    apellido = forms.CharField(max_length=30, required=True, label='Apellido')
    email = forms.EmailField(required=True )

    class Meta:
        model = User
        fields = ['username', 'nombre', 'apellido', 'email']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Password Antiguo', widget=forms.PasswordInput)
    new_password1 = forms.RegexField(label="Password nuevo", regex=r'^[\w.@+-]+$', min_length=5,
                                     widget=forms.PasswordInput,
                                     help_text='Minimo 5 carateres. Letras, digitos y @/./+/-/_ solamente.')


    new_password2 = forms.RegexField(label="Password nuevo (confirmacion)", regex=r'^[\w.@+-]+$', min_length=5,
                                 widget=forms.PasswordInput)
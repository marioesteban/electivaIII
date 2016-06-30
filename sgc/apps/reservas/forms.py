import itertools

from django import forms
from django.utils.text import slugify
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


from apps.usuarios.models import Usuario
from apps.proyectos import Reserva


class ReservaCreateForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(User.objects.exclude(is_staff=True))

    class Meta:
        model = Reserva
        fields = ['nombre_corto', 'odontologo', 'usuario', 'fecha', 'hora', 'estado']

    def clean_fecha_fin(self):
        reservas = Reserva.objects.all()
        fecha = self.cleaned_data['fecha']
        hora = self.cleaned_data['hora']
        for reserva in reservas:
            if fecha == reserva.fecha:
                if hora == reserva.hora:
                    raise forms.ValidationError("Verifique la fecha de reserva.")

        return fecha, hora

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("No se puede crear la Reserva")
        reserva = super(ReservaCreateForm, self).save(commit=True)
        usuario = User.objects.get(pk=self.cleaned_data['usuario'].pk)

        #grupo = Group.objects.get(name='Scrum Master')
        #Se agrega al usuario al equipo



        return reserva



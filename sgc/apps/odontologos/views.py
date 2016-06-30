from django.shortcuts import render
from models import Odontologo
from django.views import generic
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView
from forms import OdontologoCreateForm
class listarOdontologos(generic.ListView):
    """
    Clase que despliega la lista completa de Odontologos en el Index
    de la aplicacion Odontologos


    """
    model = Odontologo
    template_name = 'odontologos/index.html'
    form_class = OdontologoCreateForm


class crearOdontologo(CreateView):
    """
    Clase que despliega el formulario para la creacion de Odontologos.

    """
    model = Odontologo
    template_name = 'odontologos/crear.html'
    fields = ['nombre','especialidad','correoElectronico','telefono','direccion']

    
       

    def get_success_url(self):
        """
        Metodo que redirecciona al index de odontologos una vez que los datos se hayan guardado correctamente.

        """
        return reverse('odontologos:index')


class actualizarOdontologo(UpdateView):
    """
    Clase que despliega el formulario para la modficacion de Odontologos.

    """
    model = Odontologo
    template_name = 'odontologos/actualizar.html'

    def get_object(self, queryset=None):
        obj = Odontologo.objects.get(pk = self.kwargs['pk'])
        return obj

    def get_success_url(self):
        """
        Metodo que redirecciona al index de Odontologos una vez que los datos se hayan guardado correctamente.

        """
        return reverse('odontologos:index')
# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse

class Odontologo(models.Model):

    """
    Clase Odontologo.
    Crea el perfil del odontologo con cada instancia. Se definen los campos nombre, especialidad,
    correo electrónico, teléfono y dirección.
    """

    nombre = models.CharField(max_length = 100, verbose_name = 'Nombre', unique = True)
    especialidad = models.CharField(max_length = 300, verbose_name = 'Especialidad')
    correoElectronico = models.EmailField(max_length = 50, verbose_name = 'Email', unique = True)
    telefono = models.CharField(max_length = 20, verbose_name = 'Telefono')
    direccion = models.CharField(max_length = 200, verbose_name = 'Direccion')

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('odontologos', kwargs={'pk': self.pk})

    class Meta:
        default_permissions = ('crear', 'modificar', 'eliminar', 'listar')
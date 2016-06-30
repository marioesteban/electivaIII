import datetime
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from apps.odontologos import Odontologo
from apps.usuarios import Usuarios

class Reserva(models.Model):
    """
    Clase Reserva.
    Crea el formulario para las reservas para cada instancia de Reserva,
    el cual define los campos codigo, nombre corto y nombre largo, fecha de inicio, fecha de fin, (estado) Cancelado,
    Scrum master, equipo, estado y cliente.
    """
    ESTADOS_RESERVA = (
        ('Pendiente', 'Pendiente'),
        ('Atendido', 'Atendido'),
    )
    nombre_corto = models.CharField(max_length=15)
    odontologo = models.ForeignKey(Odontologo, null=True, related_name='odontologo_reserva')
    usuario = models.ForeignKey(User, null=True, related_name='usuario_reserva')
    fecha = models.DateField(default=datetime.date.today)
    hora = models.IntegerField(min(8),max(17))
    asunto = models.CharField(max_length= 100)
    sintomas = models.CharField(max_length= 100)
    estado = models.CharField(max_length=15, choices=ESTADOS_RESERVA, default='Activo')



    def __unicode__(self):
        return self.nombre_corto
    
    def get_absolute_url(self):
        return reverse('reservas', kwargs={'pk': self.pk})

    class Meta:
        default_permissions = ('crear', 'modificar', 'eliminar', 'listar')

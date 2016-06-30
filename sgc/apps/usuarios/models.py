from django.db  import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractUser

class Usuario(models.Model):
    """
        Clase Usuario.
        Crea el perfil de usuario para cada instancia de la clase User,
        el cual define los campos username, password, nombre, apellido,
        email, groups. Se extiende la funcionalidad para almacenar telefono,
        direccion, para cada User existe un unico perfil de Usuario.
    """

    user = models.OneToOneField(User)
    telefono = models.CharField(max_length= 20)
    direccion = models.CharField(max_length= 50)
    User._meta.get_field('email')._unique = True
    #is_medical = models.BooleanField(default=False)
    #is_patient = models.BooleanField(default=False)

    def get_medical_profile(self):
        medical_profile = None
        if hasattr(self, 'medicalprofile'):
            medical_profile = self.medicalprofile
        return medical_profile

    def get_patient_profile(self):
        patient_profile = None
        if hasattr(self, 'patientprofile'):
            patient_profile = self.patientprofile
        return patient_profile

    def __unicode__(self):
        return self.user.get_username()

    def get_absolute_url(self):
        return reverse('usuarios', kwargs={'pk': self.pk})

    class Meta:
        default_permissions = ('crear', 'modificar', 'activar', 'inactivar', 'listar')


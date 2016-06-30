from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = patterns('apps',
                       url(r'^$', login_required(views.listarOdontologos.as_view()), name='index'),
                       url(r'^crear/$', login_required(views.crearOdontologo.as_view()), name='crear'),
                       url(r'^actualizar/(?P<pk>\d+)/$', login_required(views.actualizarOdontologo.as_view()),
                           name='actualizar'),
                       #url(r'^delete/(?P<pk_usuario>\d+)/$', 'usuarios.views.inactivar_usuario', name='delete'),
                       #url(r'^activate/(?P<pk_usuario>\d+)/$', 'usuarios.views.activar_usuario', name='activate'),
                       )
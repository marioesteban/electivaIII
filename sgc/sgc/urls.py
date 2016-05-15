"""sgc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sgc.views.home', name='home'),

    url(r'^login/$', 'sgc.views.custom_login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/login/'}, name='logout'),

    url(r'^reset/$', 'sgc.views.reset', name='reset'),
    url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'sgc.views.reset_confirm', name='reset_confirm'),
    url(r'^reset/done/$', 'sgc.views.reset_done', name='reset_done'),
    url(r'^reset/complete/$', 'sgc.views.reset_complete', name='reset_complete'),

    url(r'^perfil/$', 'sgc.views.user_profile', name='user_profile'),
    url(r'^perfil/password_change/$', 'sgc.views.perfil_change_password',
                           name='profile_password_change'),

    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


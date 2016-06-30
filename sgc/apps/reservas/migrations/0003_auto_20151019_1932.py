# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_proyecto_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='cancelado',
            field=models.BooleanField(default=True),
        ),
    ]

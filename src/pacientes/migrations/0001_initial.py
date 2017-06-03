# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('usuario', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=15)),
                ('pais', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=15)),
                ('domicilio', models.CharField(max_length=35)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=15)),
                ('Area_Medica', models.CharField(max_length=45)),
                ('Reporte_Enfermedad', models.CharField(max_length=15)),
                ('Dias_enfermo', models.IntegerField()),
                ('Comentarios', models.CharField(max_length=125)),
            ],
        ),
    ]
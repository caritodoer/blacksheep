# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-08 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsuser', '0003_auto_20170227_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolo',
            name='activo',
            field=models.BooleanField(default=False, verbose_name='Estado Confirmado'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-28 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsadmin', '0002_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='direccion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='subtitulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefono',
            field=models.CharField(max_length=50),
        ),
    ]

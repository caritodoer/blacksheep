# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-07 21:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsuser', '0003_auto_20171001_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleanalisispadre',
            name='piepagina',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='detalleanalisis',
            name='valor',
            field=models.CharField(max_length=30, null=True),
        ),
    ]

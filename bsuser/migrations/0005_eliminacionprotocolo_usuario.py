# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-28 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsuser', '0004_auto_20171007_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='eliminacionprotocolo',
            name='usuario',
            field=models.CharField(default=1, max_length=30, verbose_name='Responsable'),
            preserve_default=False,
        ),
    ]

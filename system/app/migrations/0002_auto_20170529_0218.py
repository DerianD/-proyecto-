# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='iduser',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tiempo',
            name='iduser',
            field=models.CharField(max_length=100),
        ),
    ]

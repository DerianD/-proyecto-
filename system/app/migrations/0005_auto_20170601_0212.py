# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170529_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='pcUser',
            field=models.CharField(max_length=100),
        ),
    ]

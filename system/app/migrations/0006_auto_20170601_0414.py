# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170601_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='iduser',
            field=models.IntegerField(),
        ),
    ]

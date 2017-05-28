# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iduser', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('ruta', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tiempo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iduser', models.IntegerField()),
                ('conexion', models.CharField(max_length=100)),
                ('ultimaconexion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('progreso', models.CharField(max_length=100)),
                ('edad', models.DecimalField(decimal_places=20, max_digits=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('pcUser', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]

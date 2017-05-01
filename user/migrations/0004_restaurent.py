# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Area')),
            ],
        ),
    ]

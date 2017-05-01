# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_customer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('postal_code', models.PositiveIntegerField()),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-12 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='esal',
            field=models.IntegerField(),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2016-08-02 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20160802_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='sex',
            field=models.CharField(max_length=10),
        ),
    ]
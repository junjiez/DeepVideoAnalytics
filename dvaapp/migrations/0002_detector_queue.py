# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0001_auto_20170825_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='detector',
            name='queue',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 06:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0013_indexentries_indexer_shasum'),
    ]

    operations = [
        migrations.AddField(
            model_name='retriever',
            name='source_filter',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indexer',
            name='shasum',
            field=models.CharField(max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='retriever',
            name='indexer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Indexer'),
        ),
    ]

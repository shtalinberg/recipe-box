# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-03 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.DurationField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.DurationField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='serve_with',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-01-12 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0019_auto_20161228_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='depends_string',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='questionnaire',
            field=models.CharField(choices=[('center', 'Trauma Center'), ('system', 'Trauma System')], max_length=6),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-28 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0018_auto_20161228_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='questionnaire',
            field=models.CharField(max_length=6),
        ),
    ]

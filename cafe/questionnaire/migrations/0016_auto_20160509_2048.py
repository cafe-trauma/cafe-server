# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-09 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0015_auto_20160428_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='check',
        ),
        migrations.AddField(
            model_name='answer',
            name='options',
            field=models.ManyToManyField(blank=True, to='questionnaire.Option'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-27 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0022_auto_20170726_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='org_type',
            field=models.CharField(default='center', max_length=6),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-26 18:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaire', '0021_statement_f_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activeorganization',
            name='organization',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Organization'),
        ),
        migrations.AddField(
            model_name='activeorganization',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Organization'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('organization', 'question')]),
        ),
    ]

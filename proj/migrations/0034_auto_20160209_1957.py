# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0033_remove_userlink_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='end_learning_period',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='end_work_period',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='field_of_study',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='firma',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='location',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='position',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='school',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='start_learning_period',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='start_work_period',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='title',
        ),
        migrations.AddField(
            model_name='userlink',
            name='city_1',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlink',
            name='city_2',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlink',
            name='description_1',
            field=models.CharField(default=0, max_length=350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlink',
            name='description_2',
            field=models.CharField(default=0, max_length=350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlink',
            name='firma',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlink',
            name='position',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]

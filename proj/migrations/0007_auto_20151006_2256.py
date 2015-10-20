# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0006_cv_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='end_learning_period',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='end_work_period',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='field_of_study',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='firma',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='interests',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='location',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='position',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='school',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='skills',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='start_learning_period',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='start_work_period',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='summary',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='title',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cv',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0014_cv_inter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='inter',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='interestss',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='schooll',
        ),
        migrations.AddField(
            model_name='cv',
            name='interests',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='school',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='end_learning_period',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='end_work_period',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='field_of_study',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='firma',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='location',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='position',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='skills',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='start_learning_period',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='start_work_period',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='summary',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='title',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]

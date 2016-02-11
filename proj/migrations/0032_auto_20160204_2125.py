# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0031_auto_20160204_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlink',
            name='description',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlink',
            name='field',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlink',
            name='grade',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userlink',
            name='university',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]

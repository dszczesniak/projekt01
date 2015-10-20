# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0009_auto_20151006_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='interests',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='cv',
            name='school',
            field=models.CharField(default=b'none', max_length=50),
        ),
    ]

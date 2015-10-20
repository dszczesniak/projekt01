# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0016_auto_20151006_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

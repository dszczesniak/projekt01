# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0015_auto_20151006_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='skills',
            field=models.TextField(null=True),
        ),
    ]

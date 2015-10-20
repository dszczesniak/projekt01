# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0011_auto_20151006_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='interestss',
            field=models.TextField(null=True),
        ),
    ]

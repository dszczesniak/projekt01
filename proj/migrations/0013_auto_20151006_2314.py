# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0012_auto_20151006_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='interestss',
            field=models.TextField(default=None, blank=True),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0042_auto_20160214_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlink',
            name='study_1',
            field=models.CharField(default=0, max_length=5),
        ),
    ]

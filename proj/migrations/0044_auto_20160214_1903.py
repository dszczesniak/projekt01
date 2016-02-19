# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0043_auto_20160214_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlink',
            name='study_1',
            field=models.CharField(max_length=5),
        ),
    ]

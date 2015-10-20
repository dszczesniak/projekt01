# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0004_auto_20150926_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='birth_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0048_auto_20160216_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='telephone',
            field=models.IntegerField(),
        ),
    ]

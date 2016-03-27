# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0091_auto_20160327_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]

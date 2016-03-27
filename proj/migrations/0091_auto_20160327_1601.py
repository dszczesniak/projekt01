# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0090_auto_20160327_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100000),
        ),
    ]

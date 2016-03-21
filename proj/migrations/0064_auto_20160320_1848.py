# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0063_group_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='desc',
            field=models.TextField(max_length=350),
        ),
    ]

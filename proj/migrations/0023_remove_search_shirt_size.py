# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0022_auto_20151016_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='shirt_size',
        ),
    ]

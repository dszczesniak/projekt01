# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0075_auto_20160321_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='skills',
        ),
    ]

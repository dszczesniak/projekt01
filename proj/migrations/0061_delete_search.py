# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0060_auto_20160320_1733'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Search',
        ),
    ]

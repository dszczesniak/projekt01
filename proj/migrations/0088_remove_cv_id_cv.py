# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0087_auto_20160327_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='id_cv',
        ),
    ]

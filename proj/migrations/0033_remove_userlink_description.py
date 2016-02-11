# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0032_auto_20160204_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlink',
            name='description',
        ),
    ]

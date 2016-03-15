# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0055_auto_20160308_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='date_joined',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0057_auto_20160309_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='invite_reason',
        ),
    ]

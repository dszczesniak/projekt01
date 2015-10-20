# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0010_auto_20151006_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='interests',
            new_name='interestss',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='school',
            new_name='schooll',
        ),
    ]

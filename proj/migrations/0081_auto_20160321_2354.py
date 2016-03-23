# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0080_membership_rolee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='rolee',
            new_name='role',
        ),
    ]

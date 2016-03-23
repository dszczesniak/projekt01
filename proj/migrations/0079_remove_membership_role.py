# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0078_membership_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='role',
        ),
    ]

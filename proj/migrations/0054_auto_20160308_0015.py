# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0053_skillmod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='nameGroup',
        ),
    ]

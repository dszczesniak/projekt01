# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0054_auto_20160308_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='nameGroup',
            new_name='name',
        ),
    ]

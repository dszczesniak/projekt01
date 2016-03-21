# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0061_delete_search'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='address',
            new_name='city',
        ),
    ]

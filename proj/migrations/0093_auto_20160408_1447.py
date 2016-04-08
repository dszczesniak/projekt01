# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0092_auto_20160327_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='main_language',
            new_name='main_programming_language',
        ),
    ]

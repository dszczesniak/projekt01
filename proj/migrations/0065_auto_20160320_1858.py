# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0064_auto_20160320_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='desc',
            new_name='description_of_the_group',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0065_auto_20160320_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='description_of_the_group',
            new_name='description',
        ),
    ]

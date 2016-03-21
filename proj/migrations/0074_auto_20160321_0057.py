# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0073_userskill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userskill',
            old_name='name_skill',
            new_name='skill_name',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0082_remove_membership_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='role',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]

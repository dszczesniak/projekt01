# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0056_remove_membership_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='leader',
        ),
        migrations.AddField(
            model_name='membership',
            name='leader',
            field=models.BooleanField(default=False),
        ),
    ]

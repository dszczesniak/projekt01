# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0077_auto_20160321_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='role',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]

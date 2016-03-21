# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0062_auto_20160320_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='desc',
            field=models.CharField(default=0, max_length=350),
            preserve_default=False,
        ),
    ]

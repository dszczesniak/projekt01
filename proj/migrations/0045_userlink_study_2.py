# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0044_auto_20160214_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlink',
            name='study_2',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]

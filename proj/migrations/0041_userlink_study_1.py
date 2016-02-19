# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0040_cv_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlink',
            name='study_1',
            field=models.CharField(default=0, max_length=1),
        ),
    ]

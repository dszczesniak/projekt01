# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0013_auto_20151006_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='inter',
            field=models.TextField(null=True, blank=True),
        ),
    ]

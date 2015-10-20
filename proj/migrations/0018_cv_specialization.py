# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0017_auto_20151007_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='specialization',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]

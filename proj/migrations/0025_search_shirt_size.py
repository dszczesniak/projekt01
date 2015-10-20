# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0024_auto_20151016_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='shirt_size',
            field=models.CharField(default=1, max_length=1, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large')]),
        ),
    ]

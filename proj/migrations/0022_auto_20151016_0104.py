# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0021_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='shirt_size',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large')]),
        ),
        migrations.AlterField(
            model_name='search',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

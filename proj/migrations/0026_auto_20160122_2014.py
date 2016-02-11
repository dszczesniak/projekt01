# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0025_search_shirt_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='email',
        ),
        migrations.RemoveField(
            model_name='search',
            name='name',
        ),
        migrations.RemoveField(
            model_name='search',
            name='shirt_size',
        ),
        migrations.AddField(
            model_name='search',
            name='search_text',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='search',
            name='sort',
            field=models.CharField(default=0, max_length=1, choices=[(b'C', b'----- Choose -----'), (b'N', b'Name'), (b'S', b'Surname'), (b'E', b'E-mail')]),
        ),
    ]

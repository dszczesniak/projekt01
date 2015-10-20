# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0023_remove_search_shirt_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='full_name',
        ),
        migrations.AddField(
            model_name='cv',
            name='name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='surname',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

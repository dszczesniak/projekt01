# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0019_search'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Search',
        ),
    ]

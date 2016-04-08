# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0093_auto_20160408_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='thumbnail',
        ),
    ]

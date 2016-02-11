# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0037_auto_20160209_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlink',
            name='city_2',
        ),
        migrations.RemoveField(
            model_name='userlink',
            name='description_2',
        ),
        migrations.RemoveField(
            model_name='userlink',
            name='firma',
        ),
        migrations.RemoveField(
            model_name='userlink',
            name='position',
        ),
    ]

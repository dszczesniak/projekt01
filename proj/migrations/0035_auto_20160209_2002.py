# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0034_auto_20160209_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlink',
            name='anchor',
        ),
        migrations.RemoveField(
            model_name='userlink',
            name='url',
        ),
    ]

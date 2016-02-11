# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0027_auto_20160131_2346'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userlink',
            unique_together=set([]),
        ),
    ]

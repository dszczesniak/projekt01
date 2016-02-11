# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0028_auto_20160204_1944'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userlink',
            unique_together=set([('user', 'anchor'), ('user', 'url')]),
        ),
    ]

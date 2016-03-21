# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0074_auto_20160321_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskill',
            name='skill_name',
            field=models.CharField(max_length=20),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0085_auto_20160327_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='id_cv',
            field=models.IntegerField(null=True),
        ),
    ]

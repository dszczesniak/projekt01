# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0094_remove_cv_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='birth_date',
            field=models.DateField(help_text=b'(yyyy-mm-dd)', null=True, blank=True),
        ),
    ]

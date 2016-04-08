# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0095_auto_20160408_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='birth_date',
            field=models.DateField(help_text=b'(Format yyyy-mm-dd)', null=True, blank=True),
        ),
    ]

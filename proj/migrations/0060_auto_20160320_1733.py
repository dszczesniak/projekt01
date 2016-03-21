# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0059_cv_main_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='main_language',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0084_remove_cv_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='id_cv',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='id_person',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

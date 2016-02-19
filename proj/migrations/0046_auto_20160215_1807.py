# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0045_userlink_study_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfirm',
            name='fir_1',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userfirm',
            name='fir_2',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0036_userfirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlink',
            name='description_1',
            field=models.TextField(max_length=350),
        ),
    ]

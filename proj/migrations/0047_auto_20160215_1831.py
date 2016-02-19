# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import proj.models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0046_auto_20160215_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='thumbnail',
            field=models.FileField(null=True, upload_to=proj.models.get_upload_file_name),
        ),
    ]

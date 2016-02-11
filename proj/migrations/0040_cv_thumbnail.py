# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import proj.models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0039_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='thumbnail',
            field=models.FileField(default=0, upload_to=proj.models.get_upload_file_name),
            preserve_default=False,
        ),
    ]

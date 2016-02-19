# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import proj.models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0047_auto_20160215_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='address',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='telephone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='thumbnail',
            field=models.FileField(default=0, upload_to=proj.models.get_upload_file_name, blank=True),
            preserve_default=False,
        ),
    ]

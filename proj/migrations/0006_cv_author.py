# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0005_auto_20150926_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='author',
            field=models.ForeignKey(default=2, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0070_auto_20160321_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfirm',
            name='user',
        ),
        migrations.AddField(
            model_name='userfirm',
            name='userr',
            field=models.ForeignKey(related_name='linkss', default=0, verbose_name=b'userr', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0069_auto_20160321_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfirm',
            name='userr',
        ),
        migrations.AddField(
            model_name='userfirm',
            name='user',
            field=models.ForeignKey(related_name='linkss', default=0, verbose_name=b'user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

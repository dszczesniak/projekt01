# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0058_remove_membership_invite_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='main_language',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]

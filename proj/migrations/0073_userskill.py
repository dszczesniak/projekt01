# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0072_auto_20160321_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_skill', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=30)),
                ('user', models.ForeignKey(related_name='skill', verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

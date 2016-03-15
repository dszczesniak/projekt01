# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0052_auto_20160302_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillMod',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skil', models.CharField(max_length=50)),
                ('userrr', models.ForeignKey(related_name='linksss', verbose_name=b'userrr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

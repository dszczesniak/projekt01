# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0035_auto_20160209_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFirm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firma', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('city_2', models.CharField(max_length=50)),
                ('description_2', models.CharField(max_length=350)),
                ('userr', models.ForeignKey(related_name='linkss', verbose_name=b'userr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

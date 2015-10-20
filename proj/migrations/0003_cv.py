# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0002_auto_20150903_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('telephone', models.IntegerField(max_length=15)),
                ('birth_date', models.DateTimeField(null=True, blank=True)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]

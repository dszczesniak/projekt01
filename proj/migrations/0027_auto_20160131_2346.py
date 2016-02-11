# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0026_auto_20160122_2014'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anchor', models.CharField(max_length=100, verbose_name=b'anchor text')),
                ('url', models.URLField(verbose_name=b'url')),
                ('user', models.ForeignKey(related_name='links', verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
            },
        ),
        migrations.AlterUniqueTogether(
            name='userlink',
            unique_together=set([('user', 'anchor'), ('user', 'url')]),
        ),
    ]

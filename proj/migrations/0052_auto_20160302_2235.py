# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proj', '0051_group_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b'name')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proficiency', models.IntegerField(default=10, verbose_name=b'proficiency', choices=[(b'', b'---------'), (10, b'Beginner'), (20, b'Intermediate'), (30, b'Advanced'), (40, b'Expert')])),
                ('skill', models.ForeignKey(verbose_name=b'skill', to='proj.Skill')),
                ('user', models.ForeignKey(verbose_name=b'user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user skill',
                'verbose_name_plural': 'user skills',
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'owner', through='proj.UserSkill'),
        ),
        migrations.AlterUniqueTogether(
            name='userskill',
            unique_together=set([('user', 'skill')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0068_group_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='skillmod',
            name='userrr',
        ),
        migrations.AlterUniqueTogether(
            name='userskill',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='skill',
        ),
        migrations.RemoveField(
            model_name='userskill',
            name='user',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='SkillMod',
        ),
        migrations.DeleteModel(
            name='UserSkill',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0005_auto_20151003_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mentor',
            field=models.ManyToManyField(related_name='mentor_rel_+', verbose_name=b'Mentors', to='mentor.UserProfile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mentorees',
            field=models.ManyToManyField(related_name='mentorees_rel_+', verbose_name=b'Mentorees', to='mentor.UserProfile'),
        ),
    ]

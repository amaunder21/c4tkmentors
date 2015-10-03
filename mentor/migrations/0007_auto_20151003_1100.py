# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0006_auto_20151003_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='mentor',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='mentorees',
        ),
    ]

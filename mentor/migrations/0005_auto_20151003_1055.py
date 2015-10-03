# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0004_auto_20151003_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='desires_mentor',
            field=models.BooleanField(default=False, verbose_name=b'Wants a Mentor'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='desires_mentoree',
            field=models.BooleanField(default=False, verbose_name=b'Wants a Mentoree'),
        ),
    ]

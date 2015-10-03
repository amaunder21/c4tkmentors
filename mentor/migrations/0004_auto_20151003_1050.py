# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0003_auto_20151003_1041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='dateOfBirth',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='lifeExperience',
            new_name='life_experience',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='maritalStatus',
            new_name='marital_status',
        ),
    ]

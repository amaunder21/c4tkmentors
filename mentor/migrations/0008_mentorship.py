# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0007_auto_20151003_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mentorship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mentor', models.OneToOneField(related_name='mentor', verbose_name=b'Mentor', to='mentor.UserProfile')),
                ('mentoree', models.OneToOneField(related_name='mentoree', verbose_name=b'Mentoree', to='mentor.UserProfile')),
            ],
        ),
    ]

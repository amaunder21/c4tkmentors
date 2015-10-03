# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('emailAddress', models.EmailField(max_length=254)),
                ('dateOfBirth', models.DateField()),
                ('location', models.CharField(max_length=500)),
                ('occupation', models.CharField(max_length=500)),
                ('maritalStatus', models.CharField(max_length=500, choices=[(b'married', b'Married'), (b'single', b'Single'), (b'in_a_relationship', b'In a Relationship'), (b'divorced', b'Divorced')])),
                ('kids', models.CharField(max_length=500)),
                ('education', models.CharField(max_length=500)),
                ('interests', models.TextField()),
                ('lifeExperience', models.TextField()),
                ('skills', models.TextField()),
                ('user', models.OneToOneField(verbose_name=b'The user this profile belongs to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0002_userprofile_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='emailAddress',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dateOfBirth',
            field=models.DateField(verbose_name=b'Date of Birth'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.CharField(max_length=500, verbose_name=b'Education'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.TextField(verbose_name=b'Interests'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='kids',
            field=models.CharField(max_length=500, verbose_name=b'Children'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lifeExperience',
            field=models.TextField(verbose_name=b'Life Experience'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=500, verbose_name=b'Location'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='maritalStatus',
            field=models.CharField(max_length=500, verbose_name=b'Marital Status', choices=[(b'married', b'Married'), (b'single', b'Single'), (b'in_a_relationship', b'In a Relationship'), (b'divorced', b'Divorced')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=500, verbose_name=b'Full Name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(max_length=500, verbose_name=b'Occupation'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.TextField(verbose_name=b'Skills'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(default=b'new', max_length=500, verbose_name=b'State'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(verbose_name=b'User', to=settings.AUTH_USER_MODEL),
        ),
    ]

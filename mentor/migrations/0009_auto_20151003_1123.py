# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0008_mentorship'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mentor_bio',
            field=models.TextField(null=True, verbose_name=b'Mentor Biography'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mentoree_bio',
            field=models.TextField(null=True, verbose_name=b'Mentoree Biography'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name=b'Date of Birth'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.CharField(max_length=500, null=True, verbose_name=b'Education'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.TextField(null=True, verbose_name=b'Interests'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='kids',
            field=models.CharField(max_length=500, null=True, verbose_name=b'Children'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='life_experience',
            field=models.TextField(null=True, verbose_name=b'Life Experience'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=500, null=True, verbose_name=b'Location'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='marital_status',
            field=models.CharField(max_length=500, null=True, verbose_name=b'Marital Status', choices=[(b'married', b'Married'), (b'single', b'Single'), (b'in_a_relationship', b'In a Relationship'), (b'divorced', b'Divorced')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=500, null=True, verbose_name=b'Full Name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='occupation',
            field=models.CharField(max_length=500, null=True, verbose_name=b'Occupation'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.TextField(null=True, verbose_name=b'Skills'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(default=b'new', max_length=500, verbose_name=b'State', choices=[(b'new', b'New'), (b'awaiting_match', b'Awaiting Match'), (b'matched', b'Matched')]),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0017_auto_20161027_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouttracker',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

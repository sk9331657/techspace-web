# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_remove_events_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 00:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nbasite', '0005_player_combinedname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='combinedName',
        ),
    ]

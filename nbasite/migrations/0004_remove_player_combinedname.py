# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 00:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nbasite', '0003_player_combinedname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='combinedName',
        ),
    ]
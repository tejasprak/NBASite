# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nbasite', '0006_remove_player_combinedname'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='combinedName',
            field=models.CharField(default='DefaultCombinedName', max_length=128),
            preserve_default=False,
        ),
    ]

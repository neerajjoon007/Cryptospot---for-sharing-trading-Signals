# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-28 16:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_dashconfig'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashconfig',
            name='market_image',
        ),
    ]

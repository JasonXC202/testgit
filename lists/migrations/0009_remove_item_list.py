# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-22 10:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0008_auto_20190522_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
    ]

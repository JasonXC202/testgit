# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-14 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0013_auto_20190613_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='logtime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='create_time'),
        ),
    ]
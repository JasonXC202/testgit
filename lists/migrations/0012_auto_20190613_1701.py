# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-13 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0011_auto_20190523_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='logtime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='????'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]

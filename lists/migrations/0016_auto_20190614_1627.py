# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-14 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0015_auto_20190614_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-14 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0018_auto_20190614_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(),
        ),
    ]

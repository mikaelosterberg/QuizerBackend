# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizer', '0002_auto_20161222_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='resultDate',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
    ]

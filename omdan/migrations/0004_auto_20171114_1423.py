# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 12:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omdan', '0003_auto_20171114_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='neighborhood',
            old_name='name',
            new_name='neighborhood',
        ),
    ]
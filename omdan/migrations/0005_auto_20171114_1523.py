# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('omdan', '0004_auto_20171114_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique id for this particular city in the database', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique id for this particular neighborhood in the database', primary_key=True, serialize=False),
        ),
    ]

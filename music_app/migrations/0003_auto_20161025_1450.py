# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_auto_20161025_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='genere',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.Genere'),
        ),
    ]

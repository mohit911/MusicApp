# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 10:58
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0009_auto_20161028_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='ratings',
        ),
        migrations.AddField(
            model_name='rating',
            name='music',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='music_track', to='music_app.Music'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

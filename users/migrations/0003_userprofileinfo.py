# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-05 04:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_auto_20160711_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=b'', max_length=255)),
                ('last_name', models.CharField(default=b'', max_length=255)),
                ('gender', models.CharField(choices=[(b'Others', b'Others'), (b'Male', b'Male'), (b'Female', b'Female')], max_length=8)),
                ('profile_picture', models.ImageField(upload_to=b'User/Profile Picture')),
                ('joining_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserProfileInfo',
                'verbose_name_plural': 'UserProfileInfo',
            },
        ),
    ]

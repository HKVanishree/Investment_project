# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 10:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_app', '0003_auto_20190425_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='user',
        ),
        migrations.AddField(
            model_name='organization',
            name='user',
            field=models.ManyToManyField(through='investment_app.Investment', to=settings.AUTH_USER_MODEL),
        ),
    ]

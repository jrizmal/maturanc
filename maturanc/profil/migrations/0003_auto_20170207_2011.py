# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0002_auto_20170207_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=400),
            preserve_default=False,
        ),
    ]
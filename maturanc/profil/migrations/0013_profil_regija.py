# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0012_profil_socialnaomrezja'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='regija',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialnaomrezja',
            name='google',
        ),
        migrations.RemoveField(
            model_name='socialnaomrezja',
            name='soundcloud',
        ),
    ]

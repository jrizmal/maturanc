# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-15 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0003_auto_20170207_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='socialnaomrezja',
            name='facebook',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='socialnaomrezja',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='socialnaomrezja',
            name='snapchat',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='socialnaomrezja',
            name='twitter',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]

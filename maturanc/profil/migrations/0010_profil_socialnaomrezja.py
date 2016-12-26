# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 11:12
from __future__ import unicode_literals

import annoying.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('profil', '0009_auto_20161226_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sola', models.CharField(blank=True, max_length=100, null=True)),
                ('datum_plesa', models.DateTimeField(blank=True, null=True)),
                ('starost', models.IntegerField(blank=True, null=True)),
                ('spol', models.NullBooleanField()),
                ('visina', models.IntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialnaOmrezja',
            fields=[
                ('user', annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('snapchat', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('google', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('soundcloud', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
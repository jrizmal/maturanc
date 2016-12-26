from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField


#models here:

class Profil(models.Model):
    user = AutoOneToOneField(User, primary_key=True)

    sola = models.CharField(max_length=100, blank=True)
    regija = models.CharField(max_length=100, blank=True)
    datum_plesa = models.DateTimeField(blank=True,null=True)
    starost = models.IntegerField(blank=True,null=True)
    spol = models.NullBooleanField(blank=True,null=True)
    visina = models.IntegerField(blank=True,null=True)

    bio = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.user, self.sola)
    def __unicode__(self):
        return '%s %s' % (self.user, self.sola)

class SocialnaOmrezja(models.Model):
    user = AutoOneToOneField(User, primary_key=True)

    facebook=models.CharField(max_length=100, blank=True)
    snapchat=models.CharField(max_length=100, blank=True)
    instagram=models.CharField(max_length=100, blank=True)
    google=models.CharField(max_length=100, blank=True)
    twitter=models.CharField(max_length=100, blank=True)
    soundcloud=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s' % (self.user)
    def __unicode__(self):
        return '%s' % (self.user)
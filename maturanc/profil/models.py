from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver
import os


#models here:

class Profil(models.Model):
    
    user = AutoOneToOneField(User, primary_key=True)

    sola = models.CharField(max_length=100, blank=True)
    regija = models.CharField(max_length=100, blank=True)
    datum_plesa = models.DateTimeField(blank=True,null=True)
    starost = models.DateTimeField(blank=True,null=True)
    spol = models.NullBooleanField(blank=True,null=True)
    visina = models.IntegerField(blank=True,null=True)

    bio = models.TextField(max_length=400, blank=True, default="")

    def __str__(self):
        return '%s %s' % (self.user, self.sola)
    def __unicode__(self):
        return '%s %s' % (self.user, self.sola)

class SocialnaOmrezja(models.Model):
    user = AutoOneToOneField(User, primary_key=True)

    facebook=models.CharField(max_length=100, blank=True, default="")
    snapchat=models.CharField(max_length=100, blank=True, default="")
    instagram=models.CharField(max_length=100, blank=True, default="")
    twitter=models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return '%s' % (self.user)
    def __unicode__(self):
        return '%s' % (self.user)

class ProfilnaSlika(models.Model):
    user = AutoOneToOneField(User, primary_key=True)
    slika = models.ImageField(upload_to='profilne_slike', default='default-avatar.jpg')
    slika_nalozena_cas = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' % (self.user)
    def __unicode__(self):
        return '%s' % (self.user)
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Kontakt(models.Model):
    oseba1 = models.ForeignKey(User, related_name='oseba1')
    oseba2 = models.ForeignKey(User, related_name='oseba2')
    prvi_stik = models.DateTimeField(auto_now_add=True)
    zadnji_stik = models.DateTimeField(auto_now_add=True,null=True)
    nova_sporocila = models.NullBooleanField(default=False)

    def __unicode__(self):
        return '%s: %s' % (self.oseba1, self.oseba2)

class Sporocilo(models.Model):
    posiljatelj = models.ForeignKey(User, related_name='posiljatelj')
    prejemnik = models.ForeignKey(User, related_name='prejemnik')
    besedilo = models.TextField(blank=True)
    cas_posiljanja = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s --> %s: %s' % (self.posiljatelj, self.prejemnik, self.besedilo)

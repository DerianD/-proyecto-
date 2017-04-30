from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user(models.Model):
    nombre = models.CharField(max_length=40, null=True)
    

    def __unicode__(self):
        return self.nombre
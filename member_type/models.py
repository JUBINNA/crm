#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class MemberType(models.Model):
    uid = models.CharField(max_length=20, blank=False)
    group = models.CharField(max_length=50, blank=False)
    fallow = models.CharField(max_length=20, blank=False)
    utype = models.CharField(max_length=20, blank=True)
    memo = models.TextField()

    class Meta:
        ordering = ('utype', 'group')
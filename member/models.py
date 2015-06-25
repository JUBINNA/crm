#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Member(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uid = models.CharField(max_length=20, blank=False)
    uname = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False)
    phone = models.CharField(max_length=15, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    birthday = models.DateTimeField(blank=True)
 
    class Meta:
        ordering = ('uname', 'created')
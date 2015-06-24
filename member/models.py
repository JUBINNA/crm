#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Member(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uid = models.CharField(max_length=20, blank=False)
    uname = models.CharField(max_length=50, blank=False)
    age = models.IntegerField(blank=False)
    phone = models.CharField(max_length=15, blank=True, default='')
    address = models.CharField(max_length=100, blank=True, default='')
    birthday = models.DateTimeField(blank=True)
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
 
    class Meta:
        ordering = ('uname', 'created')
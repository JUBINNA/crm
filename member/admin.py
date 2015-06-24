#-*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from member.models import Member
from member_type.models import MemberType

admin.site.register(Member)
admin.site.register(MemberType)
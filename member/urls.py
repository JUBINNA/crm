#-*- coding: utf-8 -*-
from django.conf.urls import url
from member import views

urlpatterns = [
    url(r'^member/$', views.member_list),
    url(r'^member/(?P<pk>[0-9]+)/$', views.member_detail),
]
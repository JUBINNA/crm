#-*- coding: utf-8 -*-
from django.forms import widgets
from rest_framework import serializers
from member_type.models import MemberType, LANGUAGE_CHOICES, STYLE_CHOICES


class MemberTypeSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    uid = serializers.CharField(required=True, allow_blank=False, max_length=20)
    utype = serializers.CharField(required=True, allow_blank=True, max_length=20)
    fallow = serializers.CharField(required=False, allow_blank=True, max_length=20)
    group = serializers.CharField(required=False, allow_blank=False, max_length=50)
    memo = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Member` instance, given the validated data.
        """
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Member` instance, given the validated data.
        """
        instance.uid = validated_data.get('uid', instance.uid)
        instance.utype = validated_data.get('utype', instance.utype)
        instance.fallow = validated_data.get('fallow', instance.fallow)
        instance.group = validated_data.get('group', instance.group)
        instance.memo = validated_data.get('memo', instance.memo)
        instance.save()
        return instance


#-*- coding: utf-8 -*-
from django.forms import widgets
from rest_framework import serializers
from member.models import Member, LANGUAGE_CHOICES, STYLE_CHOICES


class MemberSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    uid = serializers.CharField(required=True, allow_blank=False, max_length=20)
    uname = serializers.CharField(required=True, allow_blank=False, max_length=50)
    age = serializers.IntegerField(required=False)
    phone = serializers.CharField(required=False, allow_blank=True, max_length=15)
    address = serializers.CharField(required=False, allow_blank=True, max_length=100)
    birthday = serializers.DateTimeField(required=False)

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
        instance.uname = validated_data.get('uname', instance.uname)
        instance.age = validated_data.get('age', instance.age)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.save()
        return instance


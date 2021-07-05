import json

from rest_framework import serializers, status
from rest_framework.response import Response

from Rentcation.RentcationApp.models import UserModel, CustomerModel


class CustomerSerializer(serializers.Serializer):
    id_customer = serializers.IntegerField(source="id",required=False)
    name = serializers.CharField(allow_blank=False, allow_null=False)
    email = serializers.EmailField(max_length=20)
    password = serializers.CharField(max_length=20)
    password_confirmation = serializers.CharField(max_length=20,write_only=True)
    address = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=20)
    house_number = serializers.IntegerField()
    phone_number = serializers.IntegerField()
    class Meta:
        model = CustomerModel
        exclude = []

    def create(self, validated_data):
        respon = CustomerModel.objects.create(**validated_data)
        return respon

    def update(self, instance, validated_data):
        instance.address = validated_data['address']
        instance.city = validated_data['city']
        instance.save()
        return instance


class CustomerSerializerList(serializers.Serializer):
    id_customer = serializers.IntegerField(source='id',read_only=True)
    name = serializers.CharField(allow_blank=False, allow_null=False)
    email = serializers.EmailField(max_length=20)
    password = serializers.CharField()
    password_confirmation = serializers.CharField(write_only=True)
    address = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=20)
    house_number = serializers.IntegerField()
    phone_number = serializers.IntegerField()
    class Meta:
        model = CustomerModel
        exclude = []
from rest_framework import serializers

from Rentcation.RentcationApp.models import CategoryModel


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(write_only=True,required=False,allow_null=True)
    name = serializers.CharField(max_length=40)
    class Meta:
        model = CategoryModel

    def create(self, validated_data):
        respon = CategoryModel.objects.create(**validated_data)
        return respon

class CategorySerializerList(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=40)
    class Meta:
        model = CategoryModel

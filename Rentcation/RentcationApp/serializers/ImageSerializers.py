from rest_framework import serializers

from Rentcation.RentcationApp.models import ImageModel, ProductModel, DestinationModel


class ImageSerializerProduct(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False,allow_null=True)
    # image_id = serializers.IntegerField(source="id",required=False,read_only=True)
    id_product = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all(),required=False,allow_null=True,allow_empty=True)
    id_destination = serializers.PrimaryKeyRelatedField(queryset=DestinationModel.objects.all(),required=False,allow_null=True,allow_empty=True)
    imagebase64 = serializers.CharField(max_length=2048)
    imagename = serializers.CharField(max_length=20)
    class Meta:
        model = ImageModel
        exclude = []
    def create(self, validated_data):
        try:
            x = ImageModel.objects.get(id=10000)
            respon = ImageModel.objects.create(**validated_data)
        except:
            validated_data["id"] = 10000
            respon = ImageModel.objects.create(**validated_data)
        print("success create")
        print(respon.imagebase64)
        return respon

class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False,allow_null=True)
    id_product = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all(),required=False,allow_null=True,allow_empty=True)
    id_destination = serializers.PrimaryKeyRelatedField(queryset=DestinationModel.objects.all(), required=False,
                                                        allow_null=True, allow_empty=True)
    imagebase64 = serializers.CharField(max_length=2048)
    imagename = serializers.CharField(max_length=20)
    class Meta:
        model = ImageModel
        exclude = []

    def create(self, validated_data):
        try:
            print("image")
            print(validated_data)
            x = ImageModel.objects.get(id=10000)
            respon = ImageModel.objects.create(**validated_data)
        except:
            validated_data["id"] = 10000
            respon = ImageModel.objects.create(**validated_data)
        return None

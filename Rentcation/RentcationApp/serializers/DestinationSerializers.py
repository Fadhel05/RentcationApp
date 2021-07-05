from rest_framework import serializers

from Rentcation.RentcationApp.models import UserModel, CategoryModel, DestinationModel, ImageModel
from Rentcation.RentcationApp.serializers.ImageSerializers import ImageSerializerProduct


class DestinationSerializer(serializers.Serializer):
    id_destination = serializers.IntegerField(required=False,source="id")
    id_user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(),required=False,allow_null=True,allow_empty=True)
    id_category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all(),required=False,allow_null=True,allow_empty=True)
    images = ImageSerializerProduct(source="imagemodel_set",many=True)
    name = serializers.CharField(max_length=255)
    price = serializers.IntegerField(write_only=True)
    prices = serializers.SerializerMethodField("pricec")
    city = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=50)
    latitude = serializers.FloatField()
    longtitude = serializers.FloatField()
    description = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = DestinationModel
        exlude = []

    def create(self, validated_data):
        imageg = validated_data.pop("imagemodel_set")
        respon = DestinationModel.objects.create(**validated_data)
        querys = ImageModel.objects.all()
        if len(querys)==0:
            op = 10000
            for e in imageg:
                e['id_destination'] = respon.id
                e['id'] = op
                op = op + 1
        else:
            op=querys[::-1][0].id + 1
            for e in imageg:
                e['id_destination'] = respon.id
                e['id'] = op
                op = op + 1
        resp = ImageSerializerProduct(data=imageg,many=True)
        if resp.is_valid(raise_exception=True):
            resp.save()
        return respon


    def pricec(self,obj):
        p = obj.price
        pp = [x for x in str(p)][::-1]
        for y in range(len(pp),1,-1):
            if y%3 ==0:
                pp.insert(y,".")
        pp.pop() if pp[len(pp)-1]=="." else None
        pp = "".join(pp[::-1])
        return "Rp. " + pp
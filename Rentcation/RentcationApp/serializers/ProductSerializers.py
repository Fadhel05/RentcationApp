from collections import defaultdict

import django_filters
from rest_framework import serializers

from Rentcation.RentcationApp.models import ProductModel, UserModel, CategoryModel, ImageModel, BookingModel, \
    ReviewModel
from Rentcation.RentcationApp.serializers.CategorySerializers import CategorySerializerList
from Rentcation.RentcationApp.serializers.ImageSerializers import ImageSerializerProduct, ImageSerializer


class ProductSerializer(serializers.Serializer):
    id_product = serializers.IntegerField(source="id",required=False)
    # id_user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(),allow_null=True,allow_empty=True,required=False)
    images = ImageSerializerProduct(source="imagemodel_set",many=True)
    # imagepr = ImageSerializerProduct(source="imagemodel_set.all()",read_only=True)
    id_category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all(),allow_empty=True,allow_null=True,required=False)
    name = serializers.CharField(max_length=100)
    latitude = serializers.FloatField()
    longtitude = serializers.FloatField()
    price = serializers.IntegerField(write_only=True)
    pricee = serializers.SerializerMethodField('prices')
    description = serializers.CharField()
    created_date = serializers.DateTimeField(allow_null=True,required=False)
    class Meta:
        model = ProductModel
        exclude = []

    def prices(self,obj):
        p = obj.price
        pp = [x for x in str(p)][::-1]
        for y in range(len(pp),1,-1):
            if y%3 ==0:
                pp.insert(y,".")
        pp.pop() if pp[len(pp)-1]=="." else None
        pp = "".join(pp[::-1])
        return "Rp. " + pp


    def create(self, validated_data):
        print(validated_data)
        imageg = validated_data.pop('imagemodel_set')
        respon = ProductModel.objects.create(**validated_data)
        # for e in imageg:
        #     e['id_product'] = respon.id
        querys = ImageModel.objects.all()
        if len(querys)==0:
            op = 10000
            for e in imageg:
                e['id_product'] = respon.id
                e['id'] = op
                op = op + 1
        else:
            op=querys[::-1][0].id + 1
            for e in imageg:
                e['id_product'] = respon.id
                e['id'] = op
                op = op + 1
        resp = ImageSerializerProduct(data=imageg,many=True)
        if resp.is_valid(raise_exception=True):
            resp.save()
        # print("test")
        # print(respon.image_id.set(resp.data))
        # respon.image_id.get(id=resp.data["id"])
        # print(respon.image_id)
        return respon

class ProductSerializerList(serializers.Serializer):
    id_product = serializers.IntegerField(source="id",required=False,read_only=True)
    id_users = serializers.CharField(read_only=True,source='id_user',allow_null=True,allow_blank=True)
    id_categorys = CategorySerializerList(source="id_category")
    images = ImageSerializer(source="imagemodel_set.all",many=True)
    name = serializers.CharField(max_length=100)
    rating = serializers.SerializerMethodField("get_rating",allow_null=True)
    latitude = serializers.FloatField()
    longtitude = serializers.FloatField()
    pricee = serializers.SerializerMethodField('pricec')
    description = serializers.CharField()
    created_date = serializers.DateTimeField(allow_null=True,read_only=True)
    class Meta:
        model = ProductModel
        exclude = []
    def get_rating(self,obj):

        try:
            p = ReviewModel.objects.filter(id_booking__data_id=obj.id,id_booking__id_category__name=obj.id_category.name).values("rating")
            if len(p)>0:
                x = defaultdict(list)
                for y in list(p):
                    for a,b in y.items():
                        x[a].append(b)
                return "%.2f" % (sum(x["rating"])/len(x["rating"]))+ " / " + "5"
            return None
        except Exception as e:
            print(str(e))
            return None
    def pricec(self,obj):
        p = obj.price
        pp = [x for x in str(p)][::-1]
        for y in range(len(pp),1,-1):
            if y%3 ==0:
                pp.insert(y,".")
        pp.pop() if pp[len(pp)-1]=="." else None
        pp = "".join(pp[::-1])
        return "Rp. " + pp

from rest_framework import serializers

from Rentcation.RentcationApp.models import BookingModel, UserModel, CustomerModel, ProductModel, CategoryModel


class BookingSerializer(serializers.Serializer):
    id_booking = serializers.IntegerField(source="id",required=False)
    id_user = serializers.PrimaryKeyRelatedField(queryset=UserModel.objects.all(),allow_null=True,required=False)
    id_customer = serializers.PrimaryKeyRelatedField(queryset=CustomerModel.objects.all())
    id_category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())
    category_name = serializers.CharField(source="id_category.name",read_only=True)
    data_id = serializers.IntegerField()
    data_name = serializers.CharField()
    product_count = serializers.IntegerField()
    booking_in = serializers.DateField()
    booking_out = serializers.DateField()
    created_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = BookingModel
        exclude = []
    def create(self, validated_data):
        respon = BookingModel.objects.create(**validated_data)
        return respon
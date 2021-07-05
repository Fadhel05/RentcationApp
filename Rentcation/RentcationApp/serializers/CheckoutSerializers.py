from rest_framework import serializers

from Rentcation.RentcationApp.models import CheckoutModel, PaymentModel, BookingModel


class CheckoutSerializer(serializers.Serializer):
    id_checkout = serializers.IntegerField(source="id",required=False)
    id_booking = serializers.PrimaryKeyRelatedField(queryset=BookingModel.objects.all())
    id_payment = serializers.PrimaryKeyRelatedField(queryset=PaymentModel.objects.all())
    total_payment = serializers.IntegerField(allow_null=True)
    checkout_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = CheckoutModel
        exclude = []
    #bertanya tentang kalkulasi total payment
    def create(self, validated_data):
        respon = CheckoutModel.objects.create(**validated_data)
        return respon

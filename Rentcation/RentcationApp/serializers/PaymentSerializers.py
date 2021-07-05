from rest_framework import serializers

from Rentcation.RentcationApp.models import PaymentModel


class PaymentSerializer(serializers.Serializer):
    id_payment = serializers.IntegerField(source="id",required=False,allow_null=True)
    name = serializers.CharField()
    class Meta:
        model=PaymentModel
        exclude = []

    def create(self, validated_data):
        print(validated_data)
        respon = PaymentModel.objects.create(**validated_data)
        return respon
from rest_framework import serializers

from Rentcation.RentcationApp.models import CustomerModel, BookingModel, ReviewModel


class ReviewSerializer(serializers.Serializer):
    id_review = serializers.IntegerField(source="id",required=False)
    id_booking = serializers.PrimaryKeyRelatedField(queryset=BookingModel.objects.all())
    id_customer = serializers.PrimaryKeyRelatedField(queryset=CustomerModel.objects.all())
    rating = serializers.IntegerField()
    comment = serializers.CharField(max_length=255)
    review_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ReviewModel
        exclude = []

    def create(self, validated_data):
        respon = ReviewModel.objects.create(**validated_data)
        return respon
from rest_framework import viewsets, status
from rest_framework.response import Response

from Rentcation.RentcationApp.models import ReviewModel
from Rentcation.RentcationApp.serializers.ReviewSerializers import ReviewSerializer


class ReviewView(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer


    def create(self, request, *args, **kwargs):
        self.queryset = ReviewModel.objects.all()
        if len(self.queryset) == 0:
            request.data["id_review"] = 10000
        else:
            request.data["id_review"] = self.queryset[::-1][0].id + 1
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
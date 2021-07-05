from rest_framework import viewsets, status
from rest_framework.response import Response

from Rentcation.RentcationApp.models import BookingModel
from Rentcation.RentcationApp.serializers.BookingSerializers import BookingSerializer


class BookingView(viewsets.ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    def create(self, request, *args, **kwargs):
        self.queryset = BookingModel.objects.all()
        if len(self.queryset) == 0:
            print("p")
            request.data["id_booking"] = 10000
        else:
            request.data["id_booking"] = self.queryset[::-1][0].id + 1
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

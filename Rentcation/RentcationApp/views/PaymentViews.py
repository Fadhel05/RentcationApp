from rest_framework import viewsets, status
from rest_framework.response import Response

from Rentcation.RentcationApp.models import PaymentModel
from Rentcation.RentcationApp.serializers.PaymentSerializers import PaymentSerializer


class PaymentView(viewsets.ModelViewSet):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        self.queryset = PaymentModel.objects.all()
        if len(self.queryset)==0:
            print("p")
            request.data["id_payment"] = 10000
        else:
            request.data["id_payment"]=self.queryset[::-1][0].id + 1
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from Rentcation.RentcationApp.models import DestinationModel, ProductModel
from Rentcation.RentcationApp.serializers.DestinationSerializers import DestinationSerializer
from Rentcation.RentcationApp.serializers.ProductSerializers import ProductSerializerList


class DestinationFilter(django_filters.FilterSet):
    latitude = django_filters.NumberFilter(field_name="latitude")
    longtitude = django_filters.NumberFilter(field_name="longtitude")

    def filter_queryset(self, queryset):
        querysetproduct = ProductModel.objects.all()
        querysetdestination = DestinationModel.objects.all()
        print(self.filters)
        print(self.data["longtitude"],type(self.data["latitude"]))
        longtitude_min = float(self.data["longtitude"]) - 0.0500000
        longtitude_plus = float(self.data["longtitude"]) + 0.0500000
        latitude_min = float(self.data["latitude"]) - 0.0500000
        latitude_plus = float(self.data["latitude"]) + 0.0500000
        products = querysetproduct.filter(latitude__gte=latitude_min,latitude__lte=latitude_plus,longtitude__gte=longtitude_min,longtitude__lte=longtitude_plus )
        destinations = querysetdestination.filter(latitude__gte=latitude_min,latitude__lte=latitude_plus,longtitude__gte=longtitude_min,longtitude__lte=longtitude_plus)
        print(querysetproduct)
        print(longtitude_min)
        dataQ={"DataProduct":{},"DataDestination":{}}
        dataQ["DataProduct"]=products
        dataQ["DataDestination"]=destinations
        return dataQ
class DestinationView(viewsets.ModelViewSet):
    queryset = DestinationModel.objects.all()
    serializer_class = DestinationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DestinationFilter

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        self.queryset = DestinationModel.objects.all()
        if len(self.queryset) == 0:
            request.data["id_destination"] = 10000
        else:
            request.data["id_destination"] = self.queryset[::-1][0].id + 1
        serializer = DestinationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    @action(detail=False,methods=["get"],url_path="rekomendasi")
    def rekomendasi(self,request, *args, **kwargs):
        dataQ = {}
        print("testting")
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        #
        serializerproduct = ProductSerializerList(queryset["DataProduct"], many=True)
        serializerdestination = DestinationSerializer(queryset["DataDestination"],many=True)
        dataQ["DataProduct"]=serializerproduct.data
        dataQ["DataDestination"]=serializerdestination.data
        return Response(dataQ,status=status.HTTP_200_OK)

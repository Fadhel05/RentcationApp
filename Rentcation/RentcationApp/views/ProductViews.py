import django_filters
from django.db import models
from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from Rentcation.RentcationApp.models import ProductModel
from Rentcation.RentcationApp.serializers import ProductSerializers
from Rentcation.RentcationApp.serializers.ProductSerializers import ProductSerializerList, ProductSerializer

class ProductFilter(django_filters.FilterSet):
    id=django_filters.CharFilter(field_name="id",lookup_expr="exact")
    name=django_filters.CharFilter(field_name="name",lookup_expr="icontains")

    def filter_queryset(self, queryset):
        """
        Filter the queryset with the underlying form's `cleaned_data`. You must
        call `is_valid()` or `errors` before calling this method.

        This method should be overridden if additional filtering needs to be
        applied to the queryset before it is cached.
        """
        dataQ = {}
        if len(self.data) == 0:
            return queryset
        for name, value in self.data.items():
            if name in list(self.filters.keys()):
                dataQ[name+"__"+self.filters[name].lookup_expr] = value
        if len(dataQ) == 0:
            return "test"
        return queryset.filter(**dataQ)
        #         queryset = self.filters[name].filter(queryset, value)
        #         assert isinstance(queryset, models.QuerySet), \
        #             "Expected '%s.%s' to return a QuerySet, but got a %s instead." \
        #             % (type(self).__name__, name, type(queryset).__name__)
        #
        # return queryset


class ProductView(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializerList
    filter_backends = (DjangoFilterBackend,)
    filterset_class=ProductFilter

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if type(queryset)==str:
            return Response({"meta":{"code":400,"message":"Field tidak ada"}},status=status.HTTP_400_BAD_REQUEST)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)
    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    @action(detail=False,methods=["POST"],url_path="inputproduct")
    def InputProcut(self,request,*args,**kwargs):
        self.queryset = ProductModel.objects.all()
        if len(self.queryset) == 0:
            print("p")
            request.data["id_product"] = 10000
        else:
            request.data["id_product"] = self.queryset[::-1][0].id + 1
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



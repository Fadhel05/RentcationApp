from rest_framework import viewsets, status
from rest_framework.response import Response

from Rentcation.RentcationApp.models import CategoryModel
from Rentcation.RentcationApp.serializers.CategorySerializers import CategorySerializerList, CategorySerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializerList

    def create(self, request, *args, **kwargs):
        self.queryset = CategoryModel.objects.all()
        if len(self.queryset) == 0:
            print("p")
            request.data["id"] = 10000
        else:
            request.data["id"] = self.queryset[::-1][0].id + 1
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

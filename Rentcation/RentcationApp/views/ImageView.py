import json

from django.db import connection
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Rentcation.RentcationApp.models import ImageModel
from Rentcation.RentcationApp.serializers.ImageSerializers import ImageSerializer


class ImageView(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
@api_view(['GET','POST'])
def droptable(request):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE USER")
    success = json.dumps({'success':'success'})
    return HttpResponse(success, mimetype='application / json')
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from Rentcation.RentcationApp.models import UserModel, CustomerModel
from Rentcation.RentcationApp.serializers.CustomerSerializers import CustomerSerializer, CustomerSerializerList


class CustomerView(viewsets.ModelViewSet):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerSerializer
    # http_method_names = ['GET', 'POST', 'PUT', 'patch', 'delete', 'head', 'options', 'trace']
    def create(self, request, *args, **kwargs):
        return Response({"bad" : "request"},status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        print(self.get_object())
        return Response({"bad" : "request"},status=status.HTTP_403_FORBIDDEN)
    def partial_update(self, request, *args, **kwargs):
        return Response({"bad" : "patch"},status=status.HTTP_403_FORBIDDEN)
    def list(self, request, *args, **kwargs):
        print("list")
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        dataQ = {
            "meta":{
                "code":200,
                "Message":None
            }
        }
        serializer = CustomerSerializerList(queryset, many=True)
        dataQ["Data"]=serializer.data
        return Response(dataQ,status=status.HTTP_200_OK)
    @action(detail=False,methods=["POST"])
    def registrasi(self, request, *args, **kwargs):
        self.queryset = CustomerModel.objects.all()
        dataQ = {
            "meta":{
            "Message": None
            }
        }
        try:
            ob = self.queryset.get(email = request.data["email"])
            dataQ["meta"]["code"] = 400
            dataQ["Message"] = "Email Has Registered"
            return Response(dataQ,status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        if request.data["password"] == request.data["password_confirmation"]:
            if len(self.queryset)==0:
                request.data["id_customer"] = 10000
            else:
                request.data["id_customer"]=self.queryset[::-1][0].id + 1
                print("request")
                print(request.data)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            dataQ["meta"]["code"] = 200
            dataQ["Data"]=serializer.data
            return Response(dataQ, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["POST"])
    def login(self, request, *args, **kwargs):
        try:
            print(type(self.queryset))
            message = "email not registered"
            instance = self.queryset.filter(email=request.data['email'])
            print(instance)
            if len(instance)==0:
                instance.get(id="id")
            print("lanjut")
            message = "wrong password"
            ints = instance.get(password=request.data['password'])
            print(ints)
            serializer = self.get_serializer(ints)
            response = {
                "meta":{
                    "code":200,
                    "Message":None
                }
            }
            response["data"]=serializer.data
            return Response(response,status=status.HTTP_200_OK)
        except:
            pass
        response = {
            "meta":{
                "code":400,
                "Message":message
            }
        }
        return Response(response,status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False,methods=["put"])
    def update_location(self,request,*args,**kwargs):
        dataQ = {
            "meta": {
                "code": 200,
                "Message": "aku tampan"
            }
        }
        if len(request.data)==2 and list(request.data.keys())==["city","address"]:
            instance = self.get_object()
            # print(instance)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dataQ["Data"] = serializer.data
            return Response(dataQ,status=status.HTTP_200_OK)
        dataQ["meta"]["code"]=400
        dataQ["meta"]["Message"] = "bad request"
        return Response(dataQ,status=status.HTTP_400_BAD_REQUEST)
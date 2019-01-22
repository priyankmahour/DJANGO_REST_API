from django.shortcuts import render

from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response

#
# class OUR_ListAPIView(APIView):
#     def get(self,request,format=None):
#         qs=Employee.objects.all()
#         my_serializer=EmployeeSerializer(qs,many=True)
#         # job of EmployeeSerializer is to convert queryset to python native data type (dict)
#         # the dict data is available with (my_serializer.data)
#         # Response class is responsible for converting dict (my_serializer.data)  to JSON data
#         return Response(my_serializer.data)

from rest_framework.generics import ListAPIView

class EmployeeListAPIView(ListAPIView):
    # queryset ans serializer_class are predefined DRF words
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    # returning a response is also optional in ListAPIView

from django.shortcuts import render

from .models import Employee
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet,GenericViewSet
from .serializers import EmployeeSerializer

#
# class EmployeeCRUDCBV(ModelViewSet):
#     # ModelViewSet because it is a viewset on models
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer


#
# class EmployeeCRUDCBV(ReadOnlyModelViewSet):
#     # ReadOnlyModelViewSet because it provides implementation only for   .list   and    .retrieve
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer


from rest_framework import mixins

class My_EmployeeCRUDCBV(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

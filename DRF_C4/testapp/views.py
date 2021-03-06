from django.shortcuts import render

from .models import Employee
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet,GenericViewSet
from .serializers import EmployeeSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  AllowAny,IsAuthenticated


from .permissions import IsReadOnly,Is_get_or_patch,sunny_permission

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .authentications import CustomAuthentication

class EmployeeCRUDCBV(ModelViewSet):
    # ModelViewSet because it is a viewset on models
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    #authentication_classes=[TokenAuthentication,]
    #permission_classes=[IsReadOnly,IsAuthenticated]
    #permission_classes=[Is_get_or_patch,IsAuthenticated]
    #permission_classes=[sunny_permission,IsAuthenticated]
    authentication_classes=[JSONWebTokenAuthentication,]
    #authentication_classes=[CustomAuthentication,]
    permission_classes=[IsAuthenticated,]












#
# class EmployeeCRUDCBV(ReadOnlyModelViewSet):
#     # ReadOnlyModelViewSet because it provides implementation only for   .list   and    .retrieve
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

#
# from rest_framework import mixins
#
# class My_EmployeeCRUDCBV(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#

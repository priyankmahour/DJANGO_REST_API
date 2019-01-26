from django.shortcuts import render

from .models import Employee
from rest_framework.viewsets import ModelViewSet
from .serializers import EmployeeSerializer

class EmployeeCRUDCBV(ModelViewSet):
    # ModelViewSet because it is a viewset on models
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

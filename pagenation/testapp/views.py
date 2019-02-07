from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .serializers import EmployeeSerializer
from .models import Employee

class EmployeeListView(ListAPIView):  # pagination concept is only applicable for LIST Operation because all record will be displayed in this operation only
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
       




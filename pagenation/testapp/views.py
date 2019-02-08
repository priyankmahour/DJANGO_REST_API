from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .serializers import EmployeeSerializer
from .models import Employee

from .pagination import MyPagination,MyPagination2,MyPagination3

class EmployeeListView(ListAPIView):  # pagination concept is only applicable for LIST Operation because all record will be displayed in this operation only
    queryset=Employee.objects.all()   # queryset pap=rameter is not needed when we override get_queryset() methods
    serializer_class=EmployeeSerializer
    #pagination_class=PageNumberPagination
    #pagination_class=MyPagination2
    #pagination_class=MyPagination3
    # def get_queryset(self):
    #     qs=Employee.objects.all()
    #     name=self.request.GET.get('ename')
    #     if name is not None:                      # line 20 and 21 will only execute when ename is not none ie... ename is passes as query param
    #         qs=qs.filter(ename__icontains=name)
    #     return qs
    #search_fields=('ename',)   only ename will be searched for our input
    #search_fields=('esal','eno')  if 'esal' or 'eno' or both "esal and eno"  contains our input....  those matched  will be displayed
    # if pagenation is applied these filtered records will be displayed according to our pagination

    #search_fields=('^esal',)
    #search_fields=('=eno',)
    search_fields=('ename',)
    ordering_fields=('eno','esal',) # default value is    '__all'
    # http://127.0.0.1:8000/list-api/?myordering=-esal&mysearch=R
    # will return all records where ename contains 'R' in descending order of esal

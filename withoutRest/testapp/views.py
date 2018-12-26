from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Emp_data_view(request):
    emp_data={
               'eno':1,
               'ename':'Sunny',
               'esal':10000,
               'eaddr':'U.P'
             }
    resp='<h1>Employee Number:{}<br> Employee Name:{}<br> Employee Salary:{}<br> Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

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

import json
def Json_data_view(request):
    emp_data={
               'eno':2,
               'ename':'Monny',
               'esal':90000,
               'eaddr':'U.P'
             }
    resp=json.dumps(emp_data)
    return HttpResponse(resp,content_type='application/json')


from django.http import JsonResponse

def Json_data_view2(request):
    emp_data={
               'eno':3,
               'ename':'Dummy',
               'esal':80000,
               'eaddr':'U.P'
             }
    return JsonResponse(emp_data)

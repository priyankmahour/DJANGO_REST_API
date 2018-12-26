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


from django.views.generic import View
class JsonCBV(View):
    def get(self,request,*args,**kwargs):
          emp_data={
               'eno':4,
               'ename':'Rummy',
               'esal':70000,
               'eaddr':'U.P'
               }
          resp=json.dumps(emp_data)
          return HttpResponse(resp,content_type='application/json')

    def post(self,request,*args,**kwargs):
          emp_data={
               'eno':5,
               'ename':'Gummy',
               'esal':60000,
               'eaddr':'U.P'
               }
          resp=json.dumps(emp_data)
          return HttpResponse(resp,content_type='application/json')

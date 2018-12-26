from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from testapp.models import Employee
from django.views.generic import View
class EmployeeDetailBCBV(View):
    def get(self,request,*args,**kwargs):
       emp=Employee.objects.get(id=1)
       emp_data={
               'eno':emp.eno,
               'ename':emp.ename,
               'esal':emp.esal,
               'eaddr':emp.eaddr
             }
       resp=json.dumps(emp_data)
       return HttpResponse(resp,content_type='application/json')

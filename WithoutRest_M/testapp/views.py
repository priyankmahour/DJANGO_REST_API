from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from testapp.models import Employee
from django.views.generic import View
from django.core.serializers import serialize

class EmployeeDetailBCBV(View):
    def get(self,request,id,*args,**kwargs):
       emp=Employee.objects.get(id=id)
       '''emp_data={
               'eno':emp.eno,
               'ename':emp.ename,
               'esal':emp.esal,
               'eaddr':emp.eaddr
             }
       resp=json.dumps(emp_data)'''
       resp=serialize('json',[emp,],fields=('eno','ename','eaddr'))
       return HttpResponse(resp,content_type='application/json')



class EmployeeListCBV(View):
    def get(self,request,*args,**kwargs):
       qs=Employee.objects.all()
       resp=serialize('json',qs,fields=('eno','ename','eaddr'))
       p_data=json.loads(resp)
       final_list=[]
       for obj in p_data:
           emp_data=obj['fields']
           final_list.append(emp_data)
       resp=json.dumps(final_list)
       return HttpResponse(resp,content_type='application/json')

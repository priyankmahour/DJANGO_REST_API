from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from testapp.models import Employee
from django.views.generic import View
from django.core.serializers import serialize

from testapp.mixins import SerializeMixin,HttpResponseMixin

class EmployeeDetailBCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,id,*args,**kwargs):
      try:
          emp=Employee.objects.get(id=id)
      except Employee.DoesNotExist:
           resp=json.dumps({'msg':'Requested Page Not Found'})
           #return HttpResponse(resp,content_type='application/json',status=404)
           return self.render_to_http_response(resp,status=404)
      else:
          resp=self.myserialize([emp,])
          #return HttpResponse(resp,content_type='application/json',status=200)
          return self.render_to_http_response(resp)


class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
       qs=Employee.objects.all()
       resp=self.myserialize(qs)
       #return HttpResponse(resp,content_type='application/json')
       return self.render_to_http_response(resp)

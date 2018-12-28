from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
from testapp.models import Employee
from django.views.generic import View
from django.core.serializers import serialize
from testapp.utils import is_json
from testapp.forms import EmployeeForm

from testapp.mixins import SerializeMixin,HttpResponseMixin

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


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

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
       qs=Employee.objects.all()
       resp=self.myserialize(qs)
       #return HttpResponse(resp,content_type='application/json')
       return self.render_to_http_response(resp)

    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            resp=json.dumps({'mag':'please provide valid json data'})
            return self.render_to_http_response(resp,status=400)
        empdata=json.loads(data)
        form=EmployeeForm(data=empdata)
        if form.is_valid():
            form.save(commit=True)
            resp=json.dumps({'msg':'resource Created Successfully'})
            return self.render_to_http_response(resp)
        if form.errors:
            resp=json.dumps(form.errors)
            return self.render_to_http_response(resp,status=400)

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import json
from testapp.models import Employee
from django.views.generic import View
from django.core.serializers import serialize
from testapp.utils import is_json,get_emp_by_id
from testapp.forms import EmployeeForm

from testapp.mixins import SerializeMixin,HttpResponseMixin

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
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

    def put(self,request,id,*args,**kwargs):
        emp=get_emp_by_id(id)
        if emp is None:
            resp=json.dumps({'msg':'No Matched Resource Found, Updation Not Possible'})
            return self.render_to_http_response(resp,status=400)
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            resp=json.dumps({'msg':'please Provide valid JSON data'})
            return self.render_to_http_response(resp,status=400)
        provided_data=json.loads(data)
        original_data={
                         'eno':emp.eno,
                         'ename':emp.ename,
                         'esal':emp.esal,
                         'eaddr':emp.eaddr
                      }
        original_data.update(provided_data)
        form=EmployeeForm(data=original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            resp=json.dumps({'msg':'Record Updated Successfully'})
            return self.render_to_http_response(resp)
        if form.errors:
            resp=json.dumps(form.errors)
            return self.render_to_http_response(resp,status=400)


    def delete(self,request,id,*args,**kwargs):
        emp=get_emp_by_id(id)
        if emp is None:
            resp=json.dumps({'msg':'No Matched Resource Found, Updation Not Possible'})
            return self.render_to_http_response(resp,status=400)
        status,deleted_item=emp.delete()
        if status==1:
            resp=json.dumps({'msg':'Resource Deleted Successfully'})
            return self.render_to_http_response(resp)
        resp=json.dumps({'msg':'Some Error Occured , Unable To Delete Resource'})
        return render_to_http_response(resp,status=500)



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

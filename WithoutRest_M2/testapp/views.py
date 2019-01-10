from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from testapp.models import Student

from django.views.generic import View
import json
from testapp.utils import get_std_by_id,is_json
from testapp.mixins import HttpResponseMixin,SerializeMixin

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import StudentForm


@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUD_CBV(View,HttpResponseMixin,SerializeMixin):
    def get(self,request,*args,**kwargs):
            data=request.body
            valid_json=is_json(data)
            if not valid_json:
                resp=json.dumps({'msg':'Please Provide Valid Json'})
                return self.render_to_http_response(resp,status=400)
            pdata=json.loads(data)
            id=pdata.get('id',None)
            if id is not None:
                std=get_std_by_id(id)
                if  std is None:
                    resp=json.dumps({'msg':'No Matched Record Found'})
                    return self.render_to_http_response(resp,status=400)
                resp=self.myserialize([std,])
                return self.render_to_http_response(resp)
            qs=Student.objects.all()
            resp=self.myserialize(qs)
            return self.render_to_http_response(resp,status=200)


    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            resp=json.dumps({'msg':'Kindly Prois=de Valid JSON Data    Thank YOU !!1'})
            return self.render_to_http_response(resp,status=400)
        pdata=json.loads(data)
        form=StudentForm(pdata)
        if form.is_valid():
            form.save(commit=True)
            resp=json.dumps({'msg':'Resourse Created.'})
            return self.render_to_http_response(resp,status=200)
        if form.errors:
            resp=json.dumps(form.errors)
            return self.render_to_http_response(resp,status=400)



    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            resp=json.dumps({'msg':'Kindly Provide Valid JSON Data    Thank YOU !!1'})
            return self.render_to_http_response(resp,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            resp=json.dumps({'msg':'ID is MANDATORY For Updation !!!'})
            return self.render_to_http_response(resp,status=400)
        temp=get_std_by_id(id)
        if temp is None:
            resp=json.dumps({'msg':'No Matched Record Found'})
            return self.render_to_http_response(resp,status=400)
        original_data={
                        'rno':temp.rno,
                        'name':temp.name,
                        'marks':temp.marks,
                        'age':temp.age
                      }

        original_data.update(pdata)
        form=StudentForm(original_data,instance=temp)
        if form.is_valid():
            form.save(commit=True)
            resp=json.dumps({'msg':'Resourse Updated.'})
            return self.render_to_http_response(resp,status=200)
        if form.errors:
            resp=json.dumps(form.errors)
            return self.render_to_http_response(resp,status=400)




    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            resp=json.dumps({'msg':'Kindly Provide Valid JSON Data    Thank YOU !!1'})
            return self.render_to_http_response(resp,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            resp=json.dumps({'msg':'ID is MANDATORY For Deletion !!!'})
            return self.render_to_http_response(resp,status=400)
        std=get_std_by_id(id)
        if std is None:
            resp=json.dumps({'msg':'No Record Found With Matched ID'})
            return self.render_to_http_response(resp,status=400)
        status,deleted_item = std.delete()
        if status==1:
            resp=json.dumps({'msg':'Record Deleted'})
            return self.render_to_http_response(resp,status=400)
        else:
            resp=json.dumps({'msg':'SomeError Occured while deletion'})
            return self.render_to_http_response(resp,status=500)

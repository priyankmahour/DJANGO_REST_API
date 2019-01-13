from django.shortcuts import render

from django.http import HttpResponse
from testapp.models import Employee

from django.views.generic import View
from testapp.utils import is_json,get_emp_by_id
from testapp.mixins import HttpResponseMixin
from testapp.serializers import EmployeeSerializer

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            #resp=json.dumps({'msg':'Kindly Provide Valid Json Data . Unable To proceed !!!'})
            msg={'msg':'Kindly Provide Valid Json Data . Unable To proceed !!!'}
            resp=JSONRenderer().render(msg)
            return self.render_to_http_response(resp,status=400)
        #Parsing JSON data from employee into python data using rest_framework's  JSONParser().parse()
        my_stream=io.BytesIO(data) # converting JSON data from Client to Byte Stream
        pdata=JSONParser().parse(my_stream) # converting Byte Stream into Python data
        id=pdata.get('id',None)
        if id is not None:
            emp=get_emp_by_id(id)
            if emp is None:
                #resp=json.dumps({'msg':'No Matched Record Found. Kindly Recheck Id .'})
                msg={'msg':'No Matched Record Found. Kindly Recheck Id .'}
                resp=JSONRenderer().render(msg)
                return self.render_to_http_response(resp,status=400)

            # Serialization Comes Into Picture to convert EMP (Complex Type ) to pyhton data so that python data can be Rendered into JSON  and sent Back to Client
            eserializer_obj=EmployeeSerializer(emp)
            #eserializer_obj.data is a PYHTON Dict
            resp=JSONRenderer().render(eserializer_obj.data)
            return self.render_to_http_response(resp,status=200)
        qs=Employee.objects.all()
        eserializer_obj=EmployeeSerializer(qs,many=True)  # To serialize Query sets ... many=True  Is Necessary
        resp=JSONRenderer().render(eserializer_obj.data)
        return self.render_to_http_response(resp,status=200)


    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            resp=json.dumps({'msg':'Kindly Provide Valid Json Data . Unable To proceed !!!'})
            return self.render_to_http_response(resp,status=400)
        my_stream=io.BytesIO(data)
        pdata=JSONParser().parse(my_stream)
        my_serializer=EmployeeSerializer(data=pdata)
        if my_serializer.is_valid():
            my_serializer.save()  # Internally it will call create method
                                  # which will create Employee Object using **validated_data (my_serializer.validated_data)
            msg={'msg':'Resourse Created Successfully'}
            resp=JSONRenderer().render(msg)
            return self.render_to_http_response(resp,status=200)
        if serializer.errors:  # Just like form.errors it performs basic validations since we are using serializers instead of forms.py and SerializerMixin Class
            resp=JSONRenderer().render(serializer.errors)
            return self.render_to_http_response(resp,status=400)

    def put(self,request,*args,**kwargs):
        # by default put method always expect complete data ie.. all the fields of the record
        # if we want to provide ony partial update
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            msg={'msg':'Please Provide Valid Json'}
            resp=JSONRenderer().render(msg)
            return self.render_to_http_response(resp,status=400)
        my_stream=io.BytesIO(data)
        pdata=JSONParser().parse(my_stream)
        id=pdata.get('id',None)
        if id is None:
            msg={'msg':'ID is Needed for Updation'}
            resp=JSONRenderer().render(msg)
            return self.render_to_http_response(resp,status=400)
        emp=get_emp_by_id(id)
        if emp is None:
            msg={'msg':'No Matched Record Found'}
            resp=JSONRenderer().render(msg)
            return self.render_to_http_response(resp,status=400)
        my_serializer=EmployeeSerializer(emp,data=pdata,partial=True) # update pdata with emp instance and partial is for prtial updation
        # earlier we were able to perform partial updated with put method because we were not using any Django_rest_framework serializers
        # we were performing every task manually
        if my_serializer.is_valid():
            my_serializer.save()  # save() will  Internally it will call update Method
            msg={'msg':'Record Updated'}
            resp=JSONRenderer().render(msg)
            return self.render_to_http_response(resp,status=200)
        if my_serializer.errors:
            resp=JSONRenderer().render(my_serializer.errors)
            return self.render_to_http_response(resp,status=400)


    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            msg={'msg':'Please Provide Valid Json'}
            resp=JSONRenderer().render(msg)
            return self.render_to_http_response(resp,status=400)
        my_stream=io.BytesIO(data)
        pdata=JSONParser().parse(my_stream)
        id=pdata.get('id',None)
        if id is None:
            msg={'msg':'ID is mandatory for Deletion'}
            resp=JSONRenderer().render(msg)
            return self.render_to_http_response(resp,status=400)
        emp=get_emp_by_id(id)
        if emp is None:
            msg={'msg':'No Matched Record Found'}
            resp=JSONRenderer().render(msg)
            return self.render_to_http_response(resp,status=400)
        emp.delete()
       # There is No Role Of Serializers in Deletion Of the Record
        msg={'msg':'Resourse Deleted Successfully'}
        resp=JSONRenderer().render(msg)
        return self.render_to_http_response(resp,status=200)

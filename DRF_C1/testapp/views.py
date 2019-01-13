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

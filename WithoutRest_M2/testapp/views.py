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

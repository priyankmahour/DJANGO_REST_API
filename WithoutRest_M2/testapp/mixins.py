from django.http import HttpResponse
from testapp.models import Student
from django.core.serializers import serialize
import json

class HttpResponseMixin(object):
    def render_to_http_response(self,data,status=200):
        return HttpResponse(data,content_type="application/json",status=status)


class SerializeMixin(object):
    def myserialize(self,qs):
        json_data=serialize('json',qs)
        pdata=json.loads(json_data)
        final_list=[]
        for obj in pdata:
            a=obj['fields']
            final_list.append(a)
        json_data=json.dumps(final_list)
        return json_data

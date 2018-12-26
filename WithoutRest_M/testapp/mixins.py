import json
from django.core.serializers import serialize
from django.http import HttpResponse

class SerializeMixin(object):
    def myserialize(self,qs):
        resp=serialize('json',qs)
        p_data=json.loads(resp)
        final_list=[]
        for obj in p_data:
            emp_data=obj['fields']
            final_list.append(emp_data)
        resp=json.dumps(final_list)
        return resp

class HttpResponseMixin(object):
    def render_to_http_response(self,resp,status=200):
        return HttpResponse(resp,content_type='application/json',status=status)

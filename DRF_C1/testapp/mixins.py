from django.http import HttpResponse

class HttpResponseMixin(object):
    def render_to_http_response(self,resp,status=200):
        return HttpResponse(resp,content_type='application/json',status=status)
        

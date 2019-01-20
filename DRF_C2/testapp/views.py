from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer
#
# class TestAPIView(APIView):
#     def get(self,request,*args,**kwargs):
#         colors=['red','yellow','blue','green']
#         context={'msg':'happy Pongal','colors':colors}
#         return Response(context)
#     def post(self,request,*args,**kwargs):
#         # print(type(request.body))
#         # print(request.body)
#         # print(type(request.data))
#         # print(request.data)
#         my_serializer=NameSerializer(data=request.data)
#         if my_serializer.is_valid():
#             name=my_serializer.data.get('name')
#             msg='Hello {}, Happy Pongal'.format(name)
#             return Response({'msg':msg})
#         else:
#             return Response(my_serializer.errors,status=400)
#
#     def put(self,request,*args,**kwargs):
#         return Response({'msg':'This Message is from PUT method of APIView'})
#
#     def patch(self,request,*args,**kwargs):
#         return Response({'msg':'This Message is from PATCH method of APIView'})
#
#     def delete(self,request,*args,**kwargs):
#         return Response({'msg':'This Message is from DELETE method of APIView'})


from rest_framework.viewsets import ViewSet

class TestViewSet(ViewSet):
    def list(self,request):
         colors=['red','yellow','blue','green']
         context={'msg':'happy New Year','colors':colors}
         return Response(context)

    def create(self,request):
        my_serializer=NameSerializer(data=request.data)
        if my_serializer.is_valid():
            name=my_serializer.data.get('name')
            msg='hello {} Happy New year !! '.format(name)
            return Response({'msg':msg})
        else:
            return Response(my_serializer.errors,status=400)

    def retrieve(self,request,pk=None):
        return Response({'msg':'This is from RETRIVE method of ViewSet'})

    def update(self,request,pk=None):
        return Response({'msg':'This is from UPDATE method of ViewSet'})

    def partial_update(self,request,pk=None):
        return Response({'msg':'This is from PARTIAL_UPDATE method of ViewSet'})

    def destroy(self,request,pk=None):
        return Response({'msg':'This is from DESTROY method of ViewSet'})

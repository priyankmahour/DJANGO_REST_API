from django.shortcuts import render

from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response

#
# class OUR_ListAPIView(APIView):
#     def get(self,request,format=None):
#         qs=Employee.objects.all()
#         my_serializer=EmployeeSerializer(qs,many=True)
#         # job of EmployeeSerializer is to convert queryset to python native data type (dict)
#         # the dict data is available with (my_serializer.data)
#         # Response class is responsible for converting dict (my_serializer.data)  to JSON data
#         return Response(my_serializer.data)

from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

# class EmployeeListAPIView(ListAPIView):
#     # queryset ans serializer_class are predefined DRF words
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     # returning a response is also optional in ListAPIView




#
# class EmployeeListAPIView(ListAPIView):
#     #queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     def get_queryset(self):
#         qs=Employee.objects.all()
#         name=self.request.GET.get('ename')
#         if name is not None:
#             qs=qs.filter(ename__icontains=name)
#         return (qs)
#
# class EmployeeCreateAPIView(CreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#
#
# class EmployeeRetrieveAPIView(RetrieveAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
#
#
# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
#
#
# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
#
#
# class EmployeeListCreateAPIView(ListCreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
#     # url pattern does not require id
#     # bug fixed

# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
#
#
#
# class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'
#
#
#
#
# class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='id'






#--------------------------------
# Implementing CRUD using Mixins
#--------------------------------
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin


class EmployeeListCreateModelMixin(ListAPIView,CreateModelMixin):
      queryset=Employee.objects.all()
      serializer_class=EmployeeSerializer
      def post(self,request,*args,**kwargs):
          return self.create(request,*args,**kwargs)

      #
      # class EmployeeListCreateModelMixin(CreateAPIView,ListModelMixin):
      #        queryset=Employee.objects.all()
      #        serializer_class=EmployeeSerializer
      #        def get(self,request,*args,**kwargs):
      #            return self.list(request,*args,**kwargs)
      #
      # we could also use this for EmployeeListCreateModelMixin



class EmployeeRetrieveUpdateDestroyModelMixin(RetrieveAPIView,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin):
      queryset=Employee.objects.all()
      serializer_class=EmployeeSerializer
      lookup_field='id'
      def put(self,request,*args,**kwargs):
          return self.update(request,*args,**kwargs)
      def patch(self,request,*args,**kwargs):
          return self.partial_update(request,*args,**kwargs)
      def delete(self,request,*args,**kwargs):
          return self.destroy(request,*args,**kwargs)

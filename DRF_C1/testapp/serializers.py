from rest_framework import serializers
from testapp.models import Employee

class EmployeeSerializer(serializers.Serializer):
        eno     =serializers.IntegerField()
        ename   =serializers.CharField(max_length=128)
        esal    =serializers.IntegerField()
        eaddr   =serializers.CharField(max_length=128)
        def create(self,validated_data):
            return Employee.objects.create(**validated_data)
            

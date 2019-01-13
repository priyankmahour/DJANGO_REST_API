from rest_framework import serializers
from testapp.models import Employee

class EmployeeSerializer(serializers.Serializer):
        eno     =serializers.IntegerField()
        ename   =serializers.CharField(max_length=128)
        esal    =serializers.IntegerField()
        eaddr   =serializers.CharField(max_length=128)
        def create(self,validated_data):
            return Employee.objects.create(**validated_data)

        def update(self,instance,validated_data,partial=True):
           instance.eno=validated_data.get('eno',instance.eno)
           instance.ename=validated_data.get('ename',instance.ename)
           instance.esal=validated_data.get('esal',instance.esal)
           instance.eaddr=validated_data.get('eaddr',instance.eaddr)
           instance.save()
           return instance

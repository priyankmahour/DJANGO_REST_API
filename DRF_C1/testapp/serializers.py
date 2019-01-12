from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
        eno     =serializers.IntegerField()
        ename   =serializers.CharField(max_length=128)
        esal    =serializers.IntegerField()
        eaddr   =serializers.CharField(max_length=128)

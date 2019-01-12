from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
        eno     =models.PositiveIntegerField()
        ename   =models.CharField(max_length=128)
        esal    =models.PositiveIntegerField()
        eaddr   =models.CharField(max_length=128)

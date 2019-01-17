from rest_framework import serializers
from testapp.models import Employee

def multiple_100(value):
    print('validators Level Validation')
    if value%100 !=0:
        raise serializers.ValidationError('Employee Salary is Not multiple of 100')

class EmployeeSerializer(serializers.ModelSerializer):
    esal    =serializers.IntegerField(validators=[multiple_100])
    def validate_esal(self,value):
            print('Field Level Validation')
            if value<5000:
                    raise serializers.ValidationError('Minimun Salary is 5000')
            return value
    def validate(self,data):
            print('Object Level Validation')
            ename=data.get('ename')
            esal=data.get('esal')
            if ename.lower()=='sunny':
                if esal < 50000:
                    raise serializers.ValidationError('If Name is Sunny Min Salary is 50000')
            return data
    class Meta:
        model=Employee
        fields='__all__'


#
# class EmployeeSerializer(serializers.Serializer):
#         eno     =serializers.IntegerField()
#         ename   =serializers.CharField(max_length=128)
#         esal    =serializers.IntegerField(validators=[multiple_100])
#         eaddr   =serializers.CharField(max_length=128)
#         def create(self,validated_data):
#             return Employee.objects.create(**validated_data)
#
#         def update(self,instance,validated_data,partial=True):
#            instance.eno=validated_data.get('eno',instance.eno)
#            instance.ename=validated_data.get('ename',instance.ename)
#            instance.esal=validated_data.get('esal',instance.esal)
#            instance.eaddr=validated_data.get('eaddr',instance.eaddr)
#            instance.save()
#            return instance
#         def validate_esal(self,value):
#             print('Field Level Validation')
#             if value<5000:
#                 raise serializers.ValidationError('Minimun Salary is 5000')
#             return value
#         def validate(self,data):
#             print('Object Level Validation')
#             ename=data.get('ename')
#             esal=data.get('esal')
#             if ename=='sunny':
#                 if esal < 50000:
#                     raise serializers.ValidationError('If Name is Sunny Min Salary is 50000')
#             return data

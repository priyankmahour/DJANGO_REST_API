import json
from testapp.models import Employee

def is_json(data):
    try:
        p_data=json.loads(data)
        valid=True
    except ValueError:
        valid=False
    return valid

def get_emp_by_id(id):
    try:
        emp=Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        emp=None
    return emp

       

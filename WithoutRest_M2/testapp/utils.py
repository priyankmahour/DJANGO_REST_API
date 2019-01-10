import json
from testapp.models import Student

def is_json(data):
    try:
        pdata=json.loads(data)
        valid=True
    except ValueError:
        valid=False
    return valid


def get_std_by_id(id):

    try:
        std=Student.objects.get(id=id)
    except Student.DoesNotExist:
        std=None
    return std

    

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','pagenation.settings')

import django
django.setup()


from testapp.models import Employee
from faker import Faker
from random import *

fake=Faker()

def populate(n):
    for i in range(n):
        feno=randint(1000,9999)
        fename=fake.name()
        fesal=randint(100000,9999999)
        feaddr=fake.city()

        employee_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)

populate(120)

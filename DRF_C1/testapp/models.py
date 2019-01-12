from django.db import models


class Employee(models.Model):
    eno     =models.PositiveIntegerField()
    ename   =models.CharField(max_length=128)
    esal    =models.PositiveIntegerField()
    eaddr   =models.CharField(max_length=128)

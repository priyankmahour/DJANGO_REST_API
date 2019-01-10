from django.db import models

# Create your models here.

class Student(models.Model):
    rno     = models.PositiveIntegerField()
    name    = models.CharField(max_length=128)
    marks   = models.PositiveIntegerField()
    age     = models.PositiveIntegerField()
    

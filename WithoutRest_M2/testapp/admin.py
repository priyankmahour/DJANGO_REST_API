from django.contrib import admin

# Register your models here.
from testapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','rno','name','marks','age']

admin.site.register(Student,StudentAdmin)

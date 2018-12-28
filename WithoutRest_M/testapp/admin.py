from django.contrib import admin

# Register your models here.
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)
#https://github.com/priyankmahour/DJANGO_REST_API.git

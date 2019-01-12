from django.contrib import admin

from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)

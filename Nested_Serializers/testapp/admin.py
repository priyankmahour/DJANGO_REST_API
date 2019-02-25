from django.contrib import admin

# Register your models here.

from .models import Authors,Books


class AuthorsAdmin(admin.ModelAdmin):
    list_display=['id','f_name','l_name','subject']

class BooksAdmin(admin.ModelAdmin):
    list_display=['id','title','author','release_date','rating']

admin.site.register(Authors,AuthorsAdmin)
admin.site.register(Books,BooksAdmin)

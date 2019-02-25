from django.db import models

# Create your models here.

class Authors(models.Model):
    f_name         =models.CharField(max_length=12)
    l_name         =models.CharField(max_length=12)
    subject        =models.CharField(max_length=18)

    def __str__(self):
        return self.f_name

class Books(models.Model):
    author         =models.ForeignKey(Authors,on_delete=models.CASCADE,related_name='books_by_author')
    title          =models.CharField(max_length=28)
    release_date   =models.DateField()
    rating         =models.IntegerField()
    def __str__(self):
        return self.title

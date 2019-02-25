

from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Authors,Books
from .serializers import AuthorsSerializer,BooksSerializer

class Authors_CR(ListCreateAPIView):
    queryset=Authors.objects.all()
    serializer_class=AuthorsSerializer

class Authors_UD(RetrieveUpdateDestroyAPIView):
    queryset=Authors.objects.all()
    serializer_class=AuthorsSerializer

class Books_CR(ListCreateAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer

class Books_UD(RetrieveUpdateDestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer

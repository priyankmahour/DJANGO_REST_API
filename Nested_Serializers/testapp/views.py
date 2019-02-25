from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Authors,Books
from .serializers import AuthorsSerializer,BooksSerializer

from rest_framework.permissions import  AllowAny,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class Authors_CR(ListCreateAPIView):
    queryset=Authors.objects.all()
    serializer_class=AuthorsSerializer
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]

class Authors_UD(RetrieveUpdateDestroyAPIView):
    queryset=Authors.objects.all()
    serializer_class=AuthorsSerializer
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]

class Books_CR(ListCreateAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]

class Books_UD(RetrieveUpdateDestroyAPIView):
    queryset=Books.objects.all()
    serializer_class=BooksSerializer
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]

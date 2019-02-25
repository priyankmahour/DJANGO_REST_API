"""Nested_Serializers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from testapp import views

from rest_framework_jwt.views  import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^author/$',views.Authors_CR.as_view(),name="Authors_CR"),
    url(r'^author/(?P<pk>\d+)/$',views.Authors_UD.as_view(),name="Authors_UD"),
    url(r'^book/$',views.Books_CR.as_view(),name="Books_CR"),
    url(r'^book/(?P<pk>\d+)/$',views.Books_UD.as_view(),name="Books_UD"),

    # registring view for JWT Authentication .....
    url(r'^auth-jwt/',obtain_jwt_token,name="auth-jwt"),
    url(r'^auth-jwt-refresh/',refresh_jwt_token,name="auth-jwt-refresh"),
    url(r'^auth-jwt-verify/',verify_jwt_token,name="auth-jwt-verify"),


]

"""DRF_C3 URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/',views.EmployeeListAPIView.as_view(),name="EmployeeListAPIView"),
    #url(r'^api/',views.EmployeeCreateAPIView.as_view(),name="EmployeeCreateAPIView"),
    #url(r'^api/(?P<id>\d+)/$',views.EmployeeRetrieveAPIView.as_view(),name="EmployeeRetrieveAPIView"),
    #url(r'^api/(?P<id>\d+)/$',views.EmployeeUpdateAPIView.as_view(),name="EmployeeUpdateAPIView"),
    #url(r'^api/(?P<id>\d+)/$',views.EmployeeDestroyAPIView.as_view(),name="EmployeeDestroyAPIView"),
    #url(r'^api/$',views.EmployeeListCreateAPIView.as_view(),name="EmployeeListCreateAPIView"),
    #url(r'^api/(?P<id>\d+)/$',views.EmployeeRetrieveUpdateAPIView.as_view(),name="EmployeeRetrieveUpdateAPIView"),
    url(r'^api/(?P<id>\d+)/$',views.EmployeeRetrieveDestroyAPIView.as_view(),name="EmployeeRetrieveUpdateAPIView"),
]

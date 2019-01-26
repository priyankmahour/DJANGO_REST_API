"""DRF_C4 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from testapp import views

from rest_framework.routers import DefaultRouter
router=DefaultRouter()
# router.register('api',views.EmployeeCRUDCBV,base_name='api')      # this represents  http://127.0.0.1:8000/api/
# # base_name is optional in ModelViewSet but mandatory in normal ViewSet

router.register('api',views.My_EmployeeCRUDCBV,base_name='api')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include(router.urls)),    # this URL pattern is for     http://127.0.0.1:8000/
]

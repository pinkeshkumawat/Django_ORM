"""Practice_project URL Configuration

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
from django.conf.urls import url,re_path,include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from app1_crud.views import student_view
from app2_apiview.views import student_api
from app4_orm.views import filter_query
route = DefaultRouter()
#route.register('',)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    re_path('api1/', student_view),
    re_path('api2/', student_api),
    re_path('api4/', filter_query),
]

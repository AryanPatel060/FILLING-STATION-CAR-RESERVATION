"""fuelregistration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from main import views
from .views import GeneratePdf

urlpatterns = [  
path("",views.index,name='index'),
path("loginuser",views.loginuser,name='loginuser'),
path("signupuser",views.signupuser,name='signupuser'),
path("logout",views.logoutuser,name='logout'),
path("bookslot/<station_id>",views.bookslot,name = 'bookslot'),
path("bookslot",views.bookslot,name = 'bookslot'),
path("slotbook",views.slotbook,name = 'slotbook'),
path("profile",views.profile,name = 'profile'),
path("slotrecipe",views.slotrecipe,name = 'slotrecipe'),
path('pdf/', GeneratePdf.as_view(),name='pdf'), 


]

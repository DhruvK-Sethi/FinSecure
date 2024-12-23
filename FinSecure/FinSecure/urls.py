"""
URL configuration for FinSecure project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('register/', register, name='register'),
    path('financial-data/', submit_financial_data, name='submit_financial_data'),
    path('display-data/', display_key, name='display_key'),
    path('dashboard/', dashboard, name='dashboard'),
    path('fire_number/', fire_number, name='fire_number'),
    path('res-alloc/', investment_view, name='investment_view'),
    path('logout/', logout_view, name='logout'),


]

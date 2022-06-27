"""supermarketer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from billapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('biller/', views.billerList.as_view()),
    path('biller2/', views.billerList2.as_view()),
    path('biller3/', views.billerList3.as_view()),
    path('biller4/', views.billerList4.as_view())
]

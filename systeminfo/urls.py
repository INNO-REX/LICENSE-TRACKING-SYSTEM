"""systeminfo URL Configuration

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
from django import views
from django.contrib import admin
from django.urls import path 
from core.views import LicenseListView
from core.views import LicenseCreateview
from core.views import license_form
from core.views import notificacionMailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', LicenseListView.as_view(), name='list'),
    path('create',LicenseCreateview.as_view(),name='create'),
    path ('',license_form, name='license_form'),
    path('mail/<int:id>/', notificacionMailView.as_view(),name='mail'),
   
]

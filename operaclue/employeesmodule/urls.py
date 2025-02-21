"""
URL configuration for hrsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeeform/', views.employee_form, name='employee_form'),
    path('registration/', views.registration, name='registration'),
    path('nextofkin/', views.nextofkin, name='nextofkin'),
    # path('employee/', views.employee_list, name='employee_list'),
    path('delete/<int:id>', views.employee_form, name='employee_update'),
    path('employee_detail/<int:id>', views.employee_delete, name='employee_delete')
]

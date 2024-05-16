from django.contrib import admin

from employeesmodule.models import Employee
from employeesmodule.models import registration
from employeesmodule.models import nextofkin
# Register your models here.
admin.site.register(Employee)
admin.site.register(registration)
admin.site.register(nextofkin)
from employeesmodule.models import Employee
from employeesmodule.models import registration
from employeesmodule.models import nextofkin
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'mobile_no', 'emp_code', 'position', ]

class RegisterForm(forms.ModelForm):
    class Meta:
        model = registration
        fields = ['firstname', 'lastname', 'phone_no', 'password',]

class nextofkinForm(forms.ModelForm):
    class Meta:
        model = nextofkin
        fields = ['full_name', 'employee_name', 'ID_no', 'phone_no', ]
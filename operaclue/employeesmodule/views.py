from django.shortcuts import render, redirect

from employeesmodule.forms import EmployeeForm

from employeesmodule.forms import RegisterForm
from employeesmodule.forms import nextofkinForm
from employeesmodule.models import Employee


# Create your views here.
def employee_form(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request, 'employee_form.html',{'form':form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee/employee_list/')

# def employee_list(request):
#     context = {'employee_list':Employee.objects.all()}
#     return render(request, 'employee_list.html')

def registration(request):
    if request.method == 'GET':
        if id==0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
        return render(request, 'employee_form.html', {'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST)
        else:
         employee = Employee.objects.get(pk=id)
         form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save()
            return redirect('/employee/employee_list/')


def register_list(request):
    return render(request,template_name='registration.html')

def nextofkin(request):
    if request.method == 'GET':
        form = nextofkinForm()
        return render(request, 'nextofkin.html', context={'form':form})
    else:
        form = nextofkin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nextofkin')

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/employee_list/')
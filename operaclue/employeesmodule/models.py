from django.db import models


# Create your models here.
class Employee(models.Model):
    objects = None
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    emp_code = models.CharField(max_length=5)
    mobile_no = models.CharField(max_length=10)
    position = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name


class registration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname


class nextofkin(models.Model):
    full_name = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=20)
    ID_no = models.CharField(max_length=12)
    phone_no = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name

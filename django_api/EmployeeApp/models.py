from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    Password = models.CharField(max_length=500, default='test@123')

    def save(self,*args,**kwargs):
        self.Password=make_password(self.Password)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.EmployeeName
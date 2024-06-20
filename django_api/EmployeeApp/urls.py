from django.conf.urls import url
from EmployeeApp import views

urlpatterns=[
    url(r'^departments$',views.departmentAPi),
    url(r'^departments/([0-9]+)$',views.departmentAPi),
    url(r'^employees$',views.employeeAPi),
    url(r'^employees/([0-9]+)$',views.employeeAPi)
] 
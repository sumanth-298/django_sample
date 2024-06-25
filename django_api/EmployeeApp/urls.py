from django.conf.urls import url
from EmployeeApp import views 

urlpatterns=[
    url(r'^departments$',views.departments),
    url(r'^departments/([0-9]+)$',views.department_by_id),
    url(r'^adddepartments$',views.add_dept),
    url(r'^updatedepartments$',views.update_dept),
    url(r'^deletedepartments$',views.delete_dept),
    url(r'^employees$',views.employees),
    url(r'^employees/([0-9]+)$',views.employee_by_id),
    url(r'^addemployee$',views.add_employee),
    url(r'^updateemployee$',views.update_employee),
    url(r'^deleteemployee$',views.delete_employee),
    url(r'^validate$',views.login_view),
    # url(r'^login/$',views.login),
    # url(r'^signup/$',views.signup),
    # url(r'^reset/$',views.reset),
    # url(r'^login/signup.html$',views.signup),
    # url(r'^login/reset.html$',views.reset),
    # url(r'^login/login.html$',views.login,name='login'),
    ] 
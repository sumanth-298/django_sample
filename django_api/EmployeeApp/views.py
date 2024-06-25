from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepatrtmentSerializer,EmployeeSerializer
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
@csrf_exempt
def department_by_id(request,id=0):
    if request.method == 'GET':
        try:
            department = Departments.objects.get(DepartmentId=id)
            department_serializer = DepatrtmentSerializer(department)
            template = loader.get_template('depts.html')
            context = {
                    'mymember':department_serializer.data,
                }
            return HttpResponse(template.render(context, request))   
            return JsonResponse({"message": "Department data with given Id is retrieved successfully", 
                                     "data": department_serializer.data}, safe=False)
        except Departments.DoesNotExist:
                return JsonResponse("Department not found", safe=False)
def departments(request,id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        depatrtments_serializer = DepatrtmentSerializer(departments,many=True)
        template = loader.get_template('all_depts.html')
        context = {
                    'mydepts': depatrtments_serializer.data,
                    }
        return HttpResponse(template.render(context, request))
        return JsonResponse({"message": "Department data is retrieved successfully", 
                                        "data": depatrtments_serializer.data},safe=False)
@csrf_exempt
def add_dept(request):
    if request.method=='POST':
        department_data=JSONParser().parse(request)
        depatrtments_serializer=DepatrtmentSerializer(data=department_data)
        if depatrtments_serializer.is_valid():
            depatrtments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)

@csrf_exempt
def update_dept(request):
    if request.method=='PUT':
        department_data=JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        depatrtments_serializer=DepatrtmentSerializer(department,data=department_data)
        if depatrtments_serializer.is_valid():
            depatrtments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)

@csrf_exempt    
def delete_dept(request):
    if request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Success",safe=False)

@csrf_exempt
def employee_by_id(request,id=0):
    if request.method == 'GET':
        try:
            employee = Employees.objects.get(EmployeeId=id)
            employee_serializer = EmployeeSerializer(employee)
            template = loader.get_template('employee.html')
            context = {
                    'mymember':employee_serializer.data,
                }
            return HttpResponse(template.render(context, request)) 
            return JsonResponse({"message": "Employee data with given Id is retrieved successfully", 
                                     "data": employee_serializer.data}, safe=False)
        except Employees.DoesNotExist:
            return JsonResponse("Employee not found", safe=False)

def employees(request):            
    employees = Employees.objects.all()
    employees_serializer = EmployeeSerializer(employees, many=True)
    template = loader.get_template('all_emps.html')
    context = {
                    'mydepts': employees_serializer.data,
                    }
    return HttpResponse(template.render(context, request))
    return JsonResponse({"message": "Employee data retrieved successfully", 
                                     "data": employees_serializer.data})
        
@csrf_exempt
def add_employee(request):
    if request.method=='POST': 
        employees_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)

@csrf_exempt
def update_employee(request):
    if request.method=='PUT':
        employees_data=JSONParser().parse(request) 
        employee = Employees.objects.get(EmployeeId=employees_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employees_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)
    
@csrf_exempt
def delete_employee(request):
    if request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Success",safe=False) 

@api_view(['POST'])
def login_view(request):
    employee_name = request.data.get('EmployeeName')
    password = request.data.get('Password')
    users = Employees.objects.filter(EmployeeName=employee_name)
    if users.exists():
        for user in users:  
            if check_password(password, user.Password):
                return Response({"detail": "Login Successful"})
        return Response({"detail": "Login Unsuccessful"})  
    else:
        return Response({"detail": "User not found"})

# @api_view(['POST'])
# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         employee_name = request.POST.get('employee_name')
#         pass1 = request.POST.get('pass1')
#         print(f'Recieved name :{employee_name},pass1:{pass1}')
#         users = Employees.objects.filter(EmployeeName=employee_name)
#         if users.exists():
#             for user in users:
#                 if check_password(pass1, user.Password):
#                     employee_name = user.EmployeeName
#                     return render(request, "sample.html",{"first name":employee_name})  
#             return Response({"detail": "Login Unsuccessful"})  
#     else:
#         return render(request, "login.html")

# def signup(request):
#     return render(request,"signup.html")

# def reset(request):
#     return render(request,"reset.html")
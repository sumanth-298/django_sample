from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepatrtmentSerializer,EmployeeSerializer

@csrf_exempt
def departmentAPi(request,id=0):
    if request.method == 'GET':
        if id:
            try:
                department = Departments.objects.get(DepartmentId=id)
                department_serializer = DepatrtmentSerializer(department)
                return JsonResponse({"message": "Department data with given Id is retrieved successfully", 
                                     "data": department_serializer.data}, safe=False)
            except Departments.DoesNotExist:
                return JsonResponse("Department not found", safe=False)
        else:
            departments = Departments.objects.all()
            depatrtments_serializer = DepatrtmentSerializer(departments,many=True)
            return JsonResponse({"message": "Department data is retrieved successfully", 
                                     "data": depatrtments_serializer.data},safe=False)
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        depatrtments_serializer=DepatrtmentSerializer(data=department_data)
        if depatrtments_serializer.is_valid():
            depatrtments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        depatrtments_serializer=DepatrtmentSerializer(department,data=department_data)
        if depatrtments_serializer.is_valid():
            depatrtments_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Success",safe=False)

@csrf_exempt
def employeeAPi(request,id=0):
    if request.method == 'GET':
        if id:
            try:
                employee = Employees.objects.get(EmployeeId=id)
                employee_serializer = EmployeeSerializer(employee)
                return JsonResponse({"message": "Employee data with given Id is retrieved successfully", 
                                     "data": employee_serializer.data}, safe=False)
            except Employees.DoesNotExist:
                return JsonResponse("Employee not found", safe=False)
        else:
            employees = Employees.objects.all()
            employees_serializer = EmployeeSerializer(employees, many=True)
            return JsonResponse({"message": "Employee data retrieved successfully", 
                                     "data": employees_serializer.data})
    elif request.method=='POST':
        employees_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to add",safe=False)
    elif request.method=='PUT':
        employees_data=JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employees_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employees_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Success",safe=False)
    
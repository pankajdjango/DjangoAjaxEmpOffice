from django.shortcuts import render
from .models import EmployeeForm, OfficeForm,Office,Employee
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

def index(request):
    return render(request,"index.html")



def home(request):
    officeForm=OfficeForm()
    employeeForm=EmployeeForm()
    context={
        "officeForm" : officeForm,
        "employeeForm" : employeeForm
    }
    return render(request,'home.html',context)

def office(request):
    if request.method == 'POST':
        officeForm=OfficeForm(request.POST)
        office=officeForm.save()
        return JsonResponse (model_to_dict(office))

def employee(request):
    if request.method == 'POST':
        employeeForm=EmployeeForm(request.POST)
        employee=employeeForm.save()
        office=employee.office
        print("of",office)
        officeJson=model_to_dict(office)
        response=model_to_dict(employee)
        print(response['office'])
        response['office'] = officeJson
        print(response['office'])
        return JsonResponse (response)

def getAllOffices(request):
    offices=Office.objects.all()
    data=serializers.serialize("json",offices)
    return JsonResponse(data,safe=False)

def getAllEmployee(request):
    employee=Employee.objects.all()
    data= serializers.serialize("json",employee,use_natural_foreign_keys=True)
    return JsonResponse(data,safe=False)

def office_page(request):
    context={"officeForm":OfficeForm()}
    return render(request,template_name="office-page.html", context=context)

def employee_page(request):
    context={"employeeForm":EmployeeForm()}
    return render(request,template_name="employee-page.html", context=context)

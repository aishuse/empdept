from django.shortcuts import render,redirect
from .models import Employees,Departments
from .forms import EmployeesForm,DepartmentsForm

# Create your views here.

def create_dept(request):

    if request.method=='GET':
        form=DepartmentsForm()
        context={}
        context['form']=form
        return render(request, "create_dept.html", context)

    if request.method=="POST":
        context = {}
        form=DepartmentsForm(request.POST)
        if form.is_valid():
            form.save()
        context['form'] = form
        return render(request,"create_dept.html",context)


def create_emp(request):
    if request.method=='GET':
        form=EmployeesForm()
        context={}
        context['form']=form
        return render(request,'create_emp.html',context)
    if request.method=='POST':
        form=EmployeesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        context={}
        context['form'] = form
        return render(request, 'create_emp.html', context)

def list_emp(request):
    employees=Employees.objects.all()
    context={}
    context['employees']=employees
    return render(request,'emp.html',context)


def update_emp(request,id):
    emp=Employees.objects.get(id=id)
    if request.method=='GET':
        form=EmployeesForm(initial={'name':emp.name,'age':emp.age,'place':emp.place,'address':emp.address,'image':emp.image,'department':emp.department})
        return render(request,'update_emp.html',{'form':form})
    if request.method=='POST':
        form=EmployeesForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
        return render(request,'update_emp.html',{'form':form})


def delete_emp(request,id):
    emp=Employees.objects.get(id=id)
    emp.delete()
    # return render(request,'emp.html')
    return redirect('emp')

def detail(request,id):
    emp=Employees.objects.get(id=id)
    context={'emp':emp}
    return render(request,'details.html',context)


def list_dept(request):
    dept=Departments.objects.all()
    return render(request,'dept.html',{'dept':dept})

def update_dept(request,id):
    dept=Departments.objects.get(id=id)
    if request.method=='GET':
        form=DepartmentsForm(initial={'name':dept.name,'location':dept.location,'est_date':dept.est_date,'hod':dept.hod})
        return render(request,'update_dept.html',{'form':form})

    if request.method=='POST':
        form=DepartmentsForm(request.POST,instance=dept)
        if form.is_valid():
            form.save()
        return render(request,'update_dept.html',{'form':form})

def detail_dept(request,id):
    dept=Departments.objects.get(id=id)
    emp=dept.employees_set.all()
    return render(request,'detail_dept.html',{'emp':emp,'dept':dept})


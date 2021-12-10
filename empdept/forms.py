from django import forms
from .models import Departments
from .models import Employees

class DepartmentsForm(forms.ModelForm):
    class Meta:
        model=Departments
        fields=[
            'name',
            'location',
            'est_date',
            'hod'
        ]
        widgets={
            'est_date':forms.DateInput(attrs={"type": "date"}),
        }

class EmployeesForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields=[
            'name',
            'age',
            'place',
            'address',
            'image',
            'department'
        ]

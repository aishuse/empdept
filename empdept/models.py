from django.db import models

# Create your models here.

class Departments(models.Model):
    name=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    est_date=models.DateField()
    hod=models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Employees(models.Model):
    name=models.CharField(max_length=120)
    age=models.PositiveIntegerField(default=25)
    place=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    image=models.ImageField(upload_to='images')
    department=models.ForeignKey(Departments,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
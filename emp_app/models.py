from django.db import models
from django.forms import ModelForm


class Office(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    def natural_key(self):
        return {'pk':self.pk,'name':self.name} #+ self.author.natural_key()


class Employee(models.Model):
    genders = {
        ("M" ,"Male"),
        ("F" ,"Female")
    }
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20,choices=genders)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name +" "+self.last_name


class OfficeForm(ModelForm):
    class Meta:
        model=Office
        fields = "__all__"


class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields = "__all__"

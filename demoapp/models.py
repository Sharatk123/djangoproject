from django.db import models
from django.db.models.fields.files import FileField

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    rno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    mobile=models.CharField(max_length=255)

    def __str__ (self):
        return self.name

class Book(models.Model):
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Pdf = FileField(upload_to="pdfs/", blank=True,null=True)

    def __str__ (self):
        return self.Title

class Register(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    def __str__ (self):
        return self.name
    



    

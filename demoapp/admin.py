from django.contrib import admin
from .models import Employee,Student,Book,Register

admin.site.register(Employee)
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Register)
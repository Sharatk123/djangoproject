from django.forms import ModelForm
from .models import Student,Book

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'

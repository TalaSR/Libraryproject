from django import forms
from .models import Book, Student, Student2, Address2, StudentProfile
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']

class StudentForm2(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),
        }


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile 
        fields = ['name', 'profile_pic']
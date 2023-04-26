from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# class CreateGroupForm(forms.ModelForm):
#     class Meta:
#         model = Group
#         fields = ['title','spesification','mentor','lesson_qty','student_qty','price','time']

class CreateMentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['full_name','spesification','birth_date','country','city','adress','salary']


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name','birth_date','country','city','adress','spesification']

# class CreateUserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['username','email','first_name','last_name','birth_date','address','spesification','gender','city','country','avatar','about']

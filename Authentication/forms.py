from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from main.models import CustomUser, Teacher, Student, Grade, Subject


class SignupForm(BaseUserCreationForm):
    # other_name = forms.CharField(max_length=255)
    # phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "other_name", "phone_number"]

class TeacherSignUpForm(SignupForm):
    email = forms.EmailField()
    
    
    class Meta(SignupForm.Meta):
        model = Teacher
        fields = SignupForm.Meta.fields + ['email']
        

class StudentSignUpForm(SignupForm):
    # current_class = forms.ModelChoiceField(queryset=Grade.objects.all())
    # subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())
    
    class Meta(SignupForm.Meta):
        model = Student
        fields = SignupForm.Meta.fields

class LoginForm(forms.Form):
    identifier = forms.CharField(label='identifier', max_length=50)
    password = forms.CharField(max_length=20)
    
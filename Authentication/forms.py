from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from main.models import CustomUser, Teacher, Student, Grade, Subject


class SignupForm(BaseUserCreationForm):
    # other_name = forms.CharField(max_length=255)
    # phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "other_name", "role", "phone_number"]

class TeacherSignUpForm(SignupForm):
    email = forms.EmailField()
    level = forms.IntegerField()
    salary = forms.DecimalField()
    
    
    class Meta(SignupForm.Meta):
        fields = SignupForm.Meta.fields + ['email', 'level', 'salary']
        

class StudentSignUpForm(SignupForm):
    current_class = forms.ModelChoiceField(queryset=Grade.objects.all())
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all())
    
    
    class Meta(SignupForm.Meta):
        fields = SignupForm.Meta.fields + ['current_class', 'subjects']
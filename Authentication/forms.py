from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm
from main.models import CustomUser, Teacher, Student, Grade, Subject
from django.utils.translation import gettext_lazy as _


class SignupForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "other_name", "phone_number"]

class TeacherSignUpForm(SignupForm):
    email = forms.EmailField()
    
    
    class Meta(SignupForm.Meta):
        model = Teacher
        fields = SignupForm.Meta.fields + ['email']
        

class StudentSignUpForm(SignupForm):
    class Meta(SignupForm.Meta):
        model = Student
        fields = SignupForm.Meta.fields

class LoginForm(forms.Form):
    Reg_num = forms.CharField(label='reg_num', max_length=50)
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        "inactive": _("This account is inactive."),
    }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import User


class RegisterForm(forms.ModelForm):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    other_name = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=255)
    password_confirmation = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "firstname", "lastname",
                  "password", "password_confirmation"]

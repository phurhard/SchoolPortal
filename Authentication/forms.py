from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import User, Teacher


class RegisterForm(forms.Form):
    other_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        exclude = ["created_on", "updated_on"]

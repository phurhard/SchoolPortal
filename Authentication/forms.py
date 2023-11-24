from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from main.models import CustomUser, Teacher


class RegisterForm(BaseUserCreationForm):
    # other_name = forms.CharField(max_length=255)
    # phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "other_name", "role", "phone_number"]

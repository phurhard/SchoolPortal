from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import CustomUser, Teacher


class RegisterForm(forms.ModelForm):
    # other_name = forms.CharField(max_length=255)
    # phone_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "other_name", "password", "role", "phone_number"]

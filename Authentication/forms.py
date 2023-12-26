from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, AuthenticationForm
from main.models import CustomUser, Teacher, Student, Grade, Subject
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset


class SignupForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "other_name", "phone_number"]


class TeacherSignUpForm(SignupForm):
    email = forms.EmailField()

    class Meta(SignupForm.Meta):
        model = Teacher
        fields = SignupForm.Meta.fields + ['email']

    def __init__(self, *args, **kwargs):
        super(TeacherSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'other_name',
            'email',
            'phone_number',
            Submit('submit', 'Submit', css_class="btn btn_primary")
        )


class StudentSignUpForm(SignupForm):
    class Meta(SignupForm.Meta):
        model = Student
        fields = SignupForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super(StudentSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Signup to your student account',
                'first_name',
                'last_name',
                Submit('submit', 'Submit', css_class="btn btn_primary")
            ))


class LoginForm(forms.Form):
    reg_num = forms.CharField(label='Reg Num', max_length=50)
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

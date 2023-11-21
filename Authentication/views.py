from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from main.models import User, Teacher, Student
from .forms import RegisterForm
# Create your views here.


def index(request):
    return render(request, 'base.html')


# @require_POST
def signup(request):
    if request.method == 'POST':
        data = RegisterForm(request.POST())
        if data['phone_number']:
            user = Teacher.objects.create(**data)
        elif data['current_class']:
            user = Student.objects.create(**data)
        else:
            user = User.objects.create(**data)
        user.save()
        return redirect('/index')
    else:
        data = RegisterForm()
    return render(request, 'registration/sign_up.html', {'data': data})

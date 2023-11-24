from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
# from django.views.decorators.http import require_POST
from main.models import CustomUser, Teacher, Student
# from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import SignupForm, TeacherSignUpForm, StudentSignUpForm
# Create your views here.


def index(request):
    return HttpResponse('Authentication')


# @require_POST
def signup(request):
    if request.method == 'POST':
        data = SignupForm(request.POST)
        if data.is_valid():
            role = data.cleaned_data['role']
            if role == 'Teacher':
                teacher_form = TeacherSignUpForm(request.POST)
                if teacher_form.is_valid():
                    user = data.save()
                    teacher = teacher_form.save(commit=False)
                    teacher.user = user
                    teacher.save()
            elif role == 'Student':
                student_form = StudentSignUpForm(request.POST)
                if student_form.is_valid():
                    user = data.save()
                    student = student_form.save(commit=False)
                    student.user = user
                    student.save()
            return redirect('/home/')
    else:
        data = SignupForm()
    return render(request, 'registration/sign_up.html', {'data': data})

"""
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        user = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'other_name': request.POST.get('other_name'),
            'password': request.POST.get('password'),
            'role': request.POST.get('role'),
            'phone_number': request.POST.get('phone_number')
        }
        # will use the usercreation form here for later refactoring
        # validator(user)

        if request.POST.get('role') == 'Student':
            Student.objects.create(**user)
            print('this is a student')
        elif request.POST.get('role') == 'Teacher':
            Teacher.objects.create(**user)
            print('this is a teacher')
        else:
            print('this is a normal user which can be an administrator')
            User.objects.create(**user)
    else:
        user = UserCreationForm()
        # print(user)
    return JsonResponse(user)

"""
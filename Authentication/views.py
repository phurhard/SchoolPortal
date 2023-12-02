from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
# from django.views.decorators.http import require_POST
from main.models import CustomUser, Teacher, Student
# from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import LoginForm, TeacherSignUpForm, StudentSignUpForm
# Create your views here.


def index(request):
    return render(request, 'Authentication/index.html')

def signupTeacher(request):
    if request.method == 'POST':
        data = TeacherSignUpForm(request.POST)
        if data.is_valid():
            user = data.save()
            print(user)
            return redirect('/login')
        else:
            return redirect('auth/staff')
    else:
        data = TeacherSignUpForm()
    return render(request, 'registration/teacherPage.html', {'data': data})
    
    
def signupStudent(request):
    if request.method == 'POST':
        data = StudentSignUpForm(request.POST)
        if data.is_valid():
            user = data.save()
            print(user.id)
        
            return redirect('/login')
        else:
            return redirect('auth/student')
    else:
        data = StudentSignUpForm()
    return render(request, 'registration/studentPage.html', {'data': data})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('identifier')
            try:
                user = get_object_or_404(CustomUser, id=data)
                if user.student:
                    is_student = True
                    is_teacher = False
            except ObjectDoesNotExist:
                is_student = False
                is_teacher = True
            # print(user.__dir__())
            
            if (is_student):
                return redirect('/student')
            elif (is_teacher):
                return redirect('/staff')
            return redirect('/login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})
'''
# @require_POST
def signup_teacher(request):
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
                    user = student_form.save()
                    print(f'user {user}')
                    print(f'student form {student_form}')
                    student = student_form.save(commit=False)
                    student.user = user
                    student.save()
            return redirect('/home/')
    else:
        data = SignupForm()
    return render(request, 'registration/sign_up.html', {'data': data})
'''
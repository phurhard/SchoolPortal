from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist, ValidationError
# from django.views.decorators.http import require_POST
from main.models import CustomUser, Teacher, Student
from rest_framework.views import APIView
from .forms import LoginForm, TeacherSignUpForm, StudentSignUpForm
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from .matric_no_generator import matric_no
# Create your views here.

'''
class SignUpView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        user = CustomUser.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        
        return response
    

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = CustomUser.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "success"
        }
        return response
'''
def index(request):
    return render(request, 'Authentication/index.html')

def signupTeacher(request):
    if request.method == 'POST':
        data = TeacherSignUpForm(request.POST)
        if data.is_valid():
            user = data.save(commit=False)
            user.reg_num = matric_no(request, user)
            user.save()
            messages.success(request, f'You can use this to login {user.reg_num}')
            # print(user.to_json())
            return redirect('/login')
        else:
            return redirect('/auth/staff')
    else:
        data = TeacherSignUpForm()
    return render(request, 'registration/teacherPage.html', {'data': data})
    
    
def signupStudent(request):
    if request.method == 'POST':
        data = StudentSignUpForm(request.POST)
        if data.is_valid():
            user = data.save(commit=False)
            user.reg_num = matric_no(request, user)
            user.save()
            # print(user.id)
            messages.success(request, f'You can use this to login {user.reg_num}')
            print(messages)
            return redirect('/login')
        else:
            return redirect('/auth/student')
    else:
        data = StudentSignUpForm()
    return render(request, 'registration/studentPage.html', {'data': data})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            reg_num = form.cleaned_data.get('Reg_num')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, reg_num=reg_num, password=password)
            print(user)
            print(form.cleaned_data)
            if user is None:
                
                form.add_error(None, 'Invalid username or password')
                return render(request, 'registration/login.html', {'form': form})
            else:
                auth_login(request, user)
                # print(user)
                # print(request.user)
                try:
                    # user = get_object_or_404(CustomUser, id=data)
                    if user.is_superuser:
                        return redirect('/admin')
                    elif user.student:
                        return redirect('/student')
                except ObjectDoesNotExist:
                    return redirect('/staff')
        else:
            messages.error(request, 'Form is invalid')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/login')


# '''
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

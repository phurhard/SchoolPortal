# from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
# from django.views.decorators.http import require_POST
from main.models import User, Teacher, Student
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return HttpResponse('Authentication')


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
        # print(firstname, lastname, othername)
        
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
    return JsonResponse(user)#.to_json(), safe=False)
    # else:
    #     return JsonResponse(
    #         {
    #             'error': True,
    #             'error_message': 'Method not allowed',
    #             'status': HttpResponse.status_code
    #         }
    #     )



# # @require_POST
# def signup(request):
#     if request.method == 'POST':
#         data = RegisterForm(request.POST)
#         if data.is_valid():
#             data.save()
#             # user = Teacher.objects.create(**data)
#             # user.save()

#         # elif data.current_class:
#         #     user = Student.objects.create(**data)
#         # else:
#         #     user = User.objects.create(**data)
#             return redirect('/index')
#     else:
#         data = RegisterForm()
#     return render(request, 'registration/sign_up.html', {'data': data})

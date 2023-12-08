from django.shortcuts import render, redirect
from main.models import Student

# Create your views here.

def student_profile(request):
    '''this is the landing page for student'''
    if not request.user.is_authenticated:
        return redirect('/login')
    student = request.user
    print(f'{student.get_full_name()} {student.grade} {student.__dir__()}')
    return render(request, 'Students/studentProfile.html')

def students_list(request):
    '''Returns the list of all students'''
    if request.user.is_authenticated and request.user.is_superuser:
        students = Student.objects.all()
        return render(request, 'Students/allStudents.html', {'students': students})
    else:
        return redirect('/student')

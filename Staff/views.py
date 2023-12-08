from django.shortcuts import render, redirect
from main.models import Teacher
# Create your views here.

def index(request):
    '''this is the landing page for staffs'''
    print(request.user)
    return render(request, 'Staff/index.html')


def teacher_profile(request):
    '''Returns the profile of the teacher with the subjects taugth'''
    if not request.user.is_authenticated:
        return redirect('/login/')
    # print(f'This is the user {request.user}')
    return render(request, 'Staff/teacherProfile.html')

def teachers_list(request):
    if request.user.is_superuser and request.user.is_authenticated:
        """Only accesible to an admin"""
        all_teachers = Teacher.objects.all()
        # for teacher in all_teachers:
            # subjects = teacher.subject_set.all()
            # print(f'{teacher.get_full_name()} {teacher.reg_num} {subjects}')
        return render(request, 'Staff/allTeachers.html', {'teachers': all_teachers})
    else:
        """Return to profile page"""
        return redirect('/staff')

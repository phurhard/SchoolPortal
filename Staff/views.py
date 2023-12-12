from django.shortcuts import render, redirect
from main.models import Teacher, Subject, Student, CustomUser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    '''this is the landing page for staffs'''
    print(request.user)
    return render(request, 'Staff/index.html')


def teacher_profile(request):
    '''Returns the profile of the teacher with the subjects taugth'''
    if not request.user.is_authenticated:
        return redirect('/login/')
    user_id = request.user.id
    teacher = Teacher.objects.get(id=user_id)
    subjects = teacher.subject_set.all()
    return render(request, 'Staff/teacherProfile.html', {'teacher': teacher, 'subjects': subjects})

def teachers_list(request):
    if request.user.is_superuser and request.user.is_authenticated:
        """Only accesible to an admin"""
        all_teachers = Teacher.objects.all()
        return render(request, 'Staff/allTeachers.html', {'teachers': all_teachers})
    else:
        """Return to profile page"""
        return redirect('/staff')
    
def subjectTeacher(request, id):
    """Returns the students taking a particular subject"""
    subject = Subject.objects.get(id=id)
    print(subject)
    students = subject.student_set.all()
    print(students)
    CA =[]
    for student in students:
        for ca in student.continousassessment_set.filter(subject=subject):
            CA.append(ca)
            # print(f'{ca.total}')
    # print(f'This is the students Ca: {CA}')
    # continousassessment = student.continousassessment_set.filter()
    return render(request, 'Staff/subjectTeacher.html', {'students': students, 'subject': subject, 'continousassessment': CA})
    # pass

@csrf_exempt
def test(request):
    print('The frontend made the call')
    print(request.POST)
    return HttpResponse('Success')

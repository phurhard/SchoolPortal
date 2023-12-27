from django.shortcuts import render, redirect
from main.models import ContinousAssessment, Teacher, Subject
from django.http import Http404, HttpResponse, JsonResponse
import json
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.template import engines
from Staff.decorators import teacher_only
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    '''this is the landing page for staffs'''
    print(request.user)
    return render(request, 'Staff/index.html')


@login_required
@teacher_only
def teacher_profile(request):
    '''Returns the profile of the teacher with the subjects taugth'''
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        try:
            user_id = request.user.id
            teacher = Teacher.objects.get(id=user_id)
            subjects = teacher.subject_set.all()
        except ObjectDoesNotExist:
            raise Http404('You are not authenticated for this page')
    return render(request, 'Staff/teacherProfile.html', {'teacher': teacher, 'subjects': subjects})


@login_required
def teachers_list(request):
    if request.user.is_superuser and request.user.is_authenticated:
        """Only accesible to an admin"""
        all_teachers = Teacher.objects.all()
        return render(request, 'Staff/allTeachers.html', {'teachers': all_teachers})
    else:
        """Return to profile page"""
        return redirect('/staff')


@login_required
@teacher_only
def subjectTeacher(request, id):
    """Returns the students taking a particular subject and their respective scores in the CA"""
    subject = Subject.objects.get(id=id)
    students = subject.student_set.all()
    CA =[]
    for student in students:
        for ca in student.continousassessment_set.filter(subject=subject):
            # print(f'This is the CA id: {ca.id}')
            CA.append(ca)
    return render(request, 'Staff/subjectTeacher.html', {'students': students, 'subject': subject, 'continousassessment': CA})


@login_required
@teacher_only
def ScoresRecord(request):
    """This function is the view for editing the CA and exams of students by
    teachers it saves it to the database"""

    if request.method == 'POST':
        print(request.POST)
        data = json.loads(request.body)
        print(f'data: {data}')
        try:
            with transaction.atomic():
                for caID, caValues in data.items():
                    try:
                        CA = ContinousAssessment.objects.get(id=caID)
                        for k, v in caValues.items():
                            """This will set the values of the CA"""
                            setattr(CA, k, v)
                        CA.total = int(CA.first_ca) + int(CA.second_ca) +\
                            int(CA.third_ca) + int(CA.exams)
                        CA.save()
                    except ObjectDoesNotExist:
                        pass
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
        return JsonResponse({
            'status': 'success',
        })
    else:
        print(request.POST)
    return JsonResponse({
        'status': 'error',
        'message': "Invalid Request"
    }, status=400)

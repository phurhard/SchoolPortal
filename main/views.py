from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Teacher, Student, Subject, Grade, ContinousAssessment


def index(request):
    '''Landing page of the school portal'''
    return render(request, 'home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject_list.html', {'subjects': subjects})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'grade_list.html', {'grades': grades})

def continous_assessment_list(request):
    assessments = ContinousAssessment.objects.all()
    return render(request, 'assessment_list.html', {'assessments': assessments})

def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    return render(request, 'subject_detail.html', {'subject': subject})

def grade_detail(request, grade_id):
    grade = get_object_or_404(Grade, id=grade_id)
    return render(request, 'grade_detail.html', {'grade': grade})

def continous_assessment_detail(request, assessment_id):
    assessment = get_object_or_404(ContinousAssessment, id=assessment_id)
    return render(request, 'assessment_detail.html', {'assessment': assessment})


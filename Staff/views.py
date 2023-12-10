from django.shortcuts import render, redirect
from main.models import Teacher, Subject, Student, CustomUser
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
    print(user_id)
    print(request.user)
    # try:
    teacher = Teacher.objects.get(id=user_id)
    subjects = teacher.subject_set.all()
    # except Teacher.DoesNotExist:
        # return redirect('/login')
    # for subject in subjects:
    #     # for student in subject.students.all():
    #     print(f'{subject.subject_name}')
    #     no_of_student = len(subject.student_set.all())
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
    # continousassessment = student.continousassessment_set.filter()
    return render(request, 'Staff/subjectTeacher.html', {'students': students, 'subject': subject})
    # pass

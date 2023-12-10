from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from main.models import Student

# Create your views here.

def student_profile(request) -> HttpResponseRedirect | HttpResponsePermanentRedirect | HttpResponse:
    '''this is the landing page for student'''
    if not request.user.is_authenticated:
        return redirect(to='/login')
    return render(request, 'Students/studentProfile.html')

def students_list(request) -> HttpResponse | HttpResponseRedirect | HttpResponsePermanentRedirect:
    '''Returns the list of all students'''
    if request.user.is_authenticated and request.user.is_superuser:
        students = Student.objects.all()
        return render(request=request, template_name='Students/allStudents.html', context={'students': students})
    else:
        return redirect('/student')
def results(request, id) -> None:
    '''Returns the result of the specific student'''
    student: Student = get_object_or_404(Student, id=id)
    subjects = get_list_or_404(Subject, student=id)
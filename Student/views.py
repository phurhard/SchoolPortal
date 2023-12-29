from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from main.models import Student, Class, Subject, Grade
from django.template.loader import get_template
from django_xhtml2pdf.utils import render_to_pdf_response
import json
from .serializers import SubjectSerializers

# Create your views here.


def student_profile(request):
    '''this is the landing page for student'''
    if not request.user.is_authenticated:
        return redirect(to='/login')
    else:
        if request.user.first_login:
            return redirect(to=f'auth/{request.user.id}/change_password')
    student = request.user
    return render(request, 'Students/studentProfile.html', {'student': student})


def students_list(request):
    '''Returns the list of all students'''
    if request.user.is_authenticated and request.user.is_superuser:
        students = Student.objects.all()
        return render(request=request, template_name='Students/allStudents.html', context={'students': students})
    else:
        return redirect('/student')


def results(request, id) -> HttpResponse:
    '''Returns the result of the specific student'''
    student: Student = get_object_or_404(Student, id=id)
    return render(request, 'Students/results.html', {'student': student})


def resultToPDF(request):
    '''returns a pdf of teacher subjects'''
    # Render the Jinja template
    template_name = 'Students/result.html'
    response = HttpResponse(content_type='application/pdf')
    context = {'student': request.user.student}
    response = render_to_pdf_response(template_name, context)
    response['Content-Disposition'] = f'attachment; filename="{request.user.get_full_name()}_Report.pdf"'
    return response


def selectClass(request):
    """how to select class

    show a dropdown of all the classes, then once one is selected it should be set as the class and all other ones should not be shown

    get all classes, send it to frontend, display it as a dropdown send the
    reply via fetch to update the backend.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data['value'])

        subjects = Subject.objects.filter(subject_class=data['value'])
        print(subjects)
        # return render(request, 'Students/subjects.html', {'subjects': subjects})
        # student.current_class = data
        # print(f'class: {data}')
        subject = SubjectSerializers(subjects, many=True)
        return JsonResponse({
            'status': 'success',
            'message': 'subjects returned',
            'data': subject.data,
        }, status=200)
    else:
        classes = Grade.objects.all()
        # return JsonResponse({
        #     'status': 'success',
        #     'data': classes,
        # }, status=200)
        return render(request, 'Students/subjects.html', {'classes': classes})

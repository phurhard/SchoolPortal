from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from main.models import Student
from django.template.loader import get_template
from django_xhtml2pdf.utils import render_to_pdf_response, generate_pdf
from xhtml2pdf import pisa

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

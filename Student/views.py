from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from main.models import Student
from django.template import engines

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
    template = engines['django'].from_string(open('Student/templates/Students/result.html').read())
    html_content = template.render({'student': request.user})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'

    # Use ReportLab to convert HTML to PDF
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    # from django.http import HttpResponse

    pdf_file = response

    p = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    # from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet

    # pdf_file = response
    doc = SimpleDocTemplate(pdf_file)
    story = []

    styles = getSampleStyleSheet()

    # Add the HTML content to the PDF
    paragraphs = []
    paragraphs.extend(Paragraph(line, styles["BodyText"]) for line in html_content.splitlines())

    story.extend(paragraphs)

    doc.build(story)

    return response

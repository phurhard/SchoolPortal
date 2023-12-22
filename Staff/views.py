from django.shortcuts import render, redirect
from main.models import ContinousAssessment, Teacher, Subject, Student, CustomUser
from django.http import Http404, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import engines

# Create your views here.

def index(request):
    '''this is the landing page for staffs'''
    print(request.user)
    return render(request, 'Staff/index.html')


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
    # print(subject)
    students = subject.student_set.all()
    # print(students)
    CA =[]
    for student in students:
        for ca in student.continousassessment_set.filter(subject=subject):
            print(f'This is the CA id: {ca.id}')
            CA.append(ca)
            # print(f'{ca.total}')
    # print(f'This is the students Ca: {CA}')
    # continousassessment = student.continousassessment_set.filter()
    return render(request, 'Staff/subjectTeacher.html', {'students': students, 'subject': subject, 'continousassessment': CA})
    # pass

@csrf_exempt
def ScoresRecord(request):
    """This function is the view for editing the CA and exams of students by teachers
    it saves it to the database"""

    if request.method == 'POST':
        data = json.loads(request.body)
        for caID, caValues in data.items():
            CA = ContinousAssessment.objects.get(id=caID)
            print(CA)
            for k, v in caValues.items():
                """This will set the values of the CA"""
                # print(f'Key {k}: Value {v}')
                # print(f'This is the model of {CA}')
                # print(f'{k} = {v}')
                setattr(CA, k, v)
            CA.total = int(CA.first_ca) + int(CA.second_ca) + int(CA.third_ca) + int(CA.exams)
            # print(CA.total)
            CA.save()
    return HttpResponse('Success')

def classes(request):
    '''returns a pdf of teacher subjects'''
    # Render the Jinja template
    template = engines['django'].from_string(open('Staff/templates/Staff/classess.html').read())
    html_content = template.render({'user': request.user})

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

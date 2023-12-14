from django.urls import path
from . import views
from wkhtmltopdf.views import PDFTemplateView

urlpatterns = [
    path('student/', views.student_profile, name='home_student'),
    path('students/', views.students_list, name='student_list'),
    path('student/<int:id>/result', views.results, name='students_result'),
    path('student/pdf/', PDFTemplateView.as_view(template_name='Students/results.html', filename='result.pdf'), name='pdfResult'),
]

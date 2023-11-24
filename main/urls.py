from django.urls import path, include
from . import views
from .views import (
    index, teacher_list, student_list, subject_list, grade_list,
    continous_assessment_list, teacher_detail, student_detail,
    subject_detail, grade_detail, continous_assessment_detail
)

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', include('Authentication.urls')),
    #path('', index, name='index'),
    path('teachers/', teacher_list, name='teacher_list'),
    path('students/', student_list, name='student_list'),
    path('subjects/', subject_list, name='subject_list'),
    path('grades/', grade_list, name='grade_list'),
    path('assessments/', continous_assessment_list, name='assessment_list'),
    path('teachers/<int:teacher_id>/', teacher_detail, name='teacher_detail'),
    path('students/<int:student_id>/', student_detail, name='student_detail'),
    path('subjects/<int:subject_id>/', subject_detail, name='subject_detail'),
    path('grades/<int:grade_id>/', grade_detail, name='grade_detail'),
    path('assessments/<int:assessment_id>/', continous_assessment_detail, name='assessment_detail'),
]
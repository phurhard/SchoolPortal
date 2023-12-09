from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.teacher_profile, name='home_staff'),
    path('teachers/', views.teachers_list, name='teacher_list'),
    path('subject/students/', views.subjectTeacher, name='subjectStudents'),
]

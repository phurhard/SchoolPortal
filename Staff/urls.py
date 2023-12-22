from django.urls import path
from . import views
# make the call to a specific user with the id
urlpatterns = [
    path('staff/', views.teacher_profile, name='home_staff'),
    path('teachers/', views.teachers_list, name='teacher_list'),
    path('subject/<int:id>/students/', views.subjectTeacher, name='subjectStudents'),
    path('record/', views.ScoresRecord, name='record'),
]

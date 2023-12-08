from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_profile, name='home_student'),
    path('students/', views.students_list, name='student_list'),
    # path('sign_up/', views.signup, name='sign-up'),
]

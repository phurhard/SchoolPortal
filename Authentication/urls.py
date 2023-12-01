from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.index, name='auth'),
    path('auth/staff', views.signupTeacher, name='staffAuth_signup'),
    path('auth/student', views.signupStudent, name='studentAuth_signup'),
]

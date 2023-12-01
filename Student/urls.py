from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.index, name='home_student'),
    # path('sign_up/', views.signup, name='sign-up'),
]

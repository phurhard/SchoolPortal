from django.urls import path
from . import views

urlpatterns = [
    path('staff/', views.index, name='home_staff'),
    # path('sign_up/', views.signup, name='sign-up'),
]

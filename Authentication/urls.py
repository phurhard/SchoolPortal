from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.index, name='auth home'),
    path('sign_up/', views.signup, name='sign-up'),
]

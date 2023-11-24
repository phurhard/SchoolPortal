from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('', include('Authentication.urls')),
]

from django.urls import path
from . import views


urlpatterns = [
    # path('auth/', views.index, name='auth'),
    path('register', views.SignUpView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('user', views.UserView.as_view(), name='user'),
    
    # path('login/', views.login, name='login'),
    # path('auth/staff', views.signupTeacher, name='staffAuth_signup'),
    # path('auth/student', views.signupStudent, name='studentAuth_signup'),
]

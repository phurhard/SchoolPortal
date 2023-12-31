from django.urls import path
from . import views


urlpatterns = [
    path('auth/', views.index, name='auth'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('admin/logout/', views.user_logout, name='logout'),
    path('auth/staff/', views.signupTeacher, name='staffAuth_signup'),
    path('auth/student/', views.signupStudent, name='studentAuth_signup'),
    path('auth/<int:id>/change_password/', views.changePassword, name='change_password'),
    path('auth/forgot_password/', views.forgotPassword, name='forgot_password'),
    # path('login', views.LoginView.as_view(), name='login'),
    # path('logout', views.LogoutView.as_view(), name='logout'),
    # path('user', views.UserView.as_view(), name='user'),
]

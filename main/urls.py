from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/create_profesor/', views.create_profesor, name='create_profesor'),
   
   
    path('dashboard/create_curso/', views.create_curso, name='create_curso'),
    path('dashboard/create_alumno/', views.create_alumno, name='create_alumno'),
    path('dashboard/create_nota/', views.create_nota, name='create_nota'),

    path('register/', views.register, name='register'),
]

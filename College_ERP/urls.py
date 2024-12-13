"""
URL configuration for College_ERP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from erp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('success/', views.success_page, name='success_page'),
    path('student/', views.student_page, name='student_page'),
    path('teacher/', views.teacher_page, name='teacher_page'),

    # Custom User
    path('users/', views.custom_user_list, name='custom_user_list'),
    path('users/create/', views.custom_user_create, name='custom_user_create'),
    path('users/update/<int:pk>/', views.custom_user_update, name='custom_user_update'),
    path('users/delete/<int:pk>/', views.custom_user_delete, name='custom_user_delete'),

    # Dept
    path('departments/', views.dept_list, name='dept_list'),
    path('departments/create/', views.dept_create, name='dept_create'),
    path('departments/update/<int:pk>/', views.dept_update, name='dept_update'),
    path('departments/delete/<int:pk>/', views.dept_delete, name='dept_delete'),

    # Course
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/update/<int:pk>/', views.course_update, name='course_update'),
    path('courses/delete/<int:pk>/', views.course_delete, name='course_delete'),

    # Student
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    # Teacher
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/update/<int:pk>/', views.teacher_update, name='teacher_update'),                                                        
    path('teachers/delete/<int:pk>/', views.teacher_delete, name='teacher_delete'),

    # Assign
    path('assigns/', views.assign_list, name='assign_list'),
    path('assigns/create/', views.assign_create, name='assign_create'),
    path('assigns/update/<int:pk>/', views.assign_update, name='assign_update'),
    path('assigns/delete/<int:pk>/', views.assign_delete, name='assign_delete'),

    # Attendance
    path('attendances/', views.attendance_list, name='attendance_list'),
    path('attendances/create/', views.attendance_create, name='attendance_create'),
    path('attendances/update/<int:pk>/', views.attendance_update, name='attendance_update'),
    path('attendances/delete/<int:pk>/', views.attendance_delete, name='attendance_delete'),
]



from django.contrib import admin
from .models import CustomUser, Dept, Course, Class, Student, Teacher, Assign, AssignTime, AttendanceClass, Attendance

# Register your models here.



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_student', 'is_teacher', 'date_joined']
    
@admin.register(Dept)
class DeptAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'dept', 'name', 'shortname']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'dept', 'section', 'sem']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'class_id', 'USN', 'enrollment_no', 'dob', 'gender']
    search_fields = ['user__email', 'USN', 'enrollment_no']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'dept', 'dob', 'gender']
    search_fields = ['user__email', 'id']

@admin.register(Assign)
class AssignAdmin(admin.ModelAdmin):
    list_display = ['class_id', 'course', 'teacher']
    search_fields = ['class_id__id', 'course__name', 'teacher__user__email']

@admin.register(AssignTime)
class AssignTimeAdmin(admin.ModelAdmin):
    list_display = ['assign', 'period', 'day']

@admin.register(AttendanceClass)
class AttendanceClassAdmin(admin.ModelAdmin):
    list_display = ['assign', 'date', 'status']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['attendance_class', 'student', 'date', 'status']

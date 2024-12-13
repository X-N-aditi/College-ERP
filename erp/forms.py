from django import forms
from .models import CustomUser, Dept, Course, Class, Student, Teacher, Assign, AssignTime, AttendanceClass, Attendance
from django.contrib.auth.forms import AuthenticationForm


# Form for CustomUser model
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_student', 'is_teacher']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.Select(attrs={'class': 'form-control'}),
            'is_staff': forms.Select(attrs={'class': 'form-control'}),
            'is_student': forms.Select(attrs={'class': 'form-control'}),
            'is_teacher': forms.Select(attrs={'class': 'form-control'}),
        }
        
# Form for Dept model
class DeptForm(forms.ModelForm):
    class Meta:
        model = Dept
        fields = ['id', 'name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department Name'}),
        }

# Form for Course model
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['id', 'dept', 'name', 'shortname']
        widgets = {
            'dept': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'shortname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Short Name'}),
        }

# Form for Class model
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['id', 'dept', 'section', 'sem']
        widgets = {
            'dept': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Section'}),
            'sem': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Semester'}),
        }

# Form for Student model
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'password', 'class_id', 'USN', 'enrollment_no', 'dob', 'gender']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'class_id': forms.Select(attrs={'class': 'form-control'}),
            'USN': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'USN'}),
            'enrollment_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enrollment Number'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

# Form for Teacher model
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'password', 'id', 'dept', 'dob', 'gender']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teacher ID'}),
            'dept': forms.Select(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

# Form for Assign model
class AssignForm(forms.ModelForm):
    class Meta:
        model = Assign
        fields = ['class_id', 'course', 'teacher']
        widgets = {
            'class_id': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
        }

# Form for AssignTime model
class AssignTimeForm(forms.ModelForm):
    class Meta:
        model = AssignTime
        fields = ['assign', 'period', 'day']
        widgets = {
            'assign': forms.Select(attrs={'class': 'form-control'}),
            'period': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Period'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
        }

# Form for AttendanceClass model
class AttendanceClassForm(forms.ModelForm):
    class Meta:
        model = AttendanceClass
        fields = ['assign', 'date', 'status']
        widgets = {
            'assign': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

# Form for Attendance model
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

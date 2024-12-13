from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import CustomUser, Dept, Course, Class, Student, Teacher, Assign, AssignTime, AttendanceClass, Attendance
from .forms import CustomUserForm, DeptForm, CourseForm, ClassForm, StudentForm, TeacherForm, AssignForm, AssignTimeForm, AttendanceClassForm, AttendanceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate



# Home view
def home(request):
    return render(request, 'erp/home.html')

def success_page(request):
    return render(request, 'erp/success_page.html')

#---------------------------------------------
def teacher_page(request):
    return render(request, 'erp/teacher_page.html')

def student_page(request):
    return render(request, 'erp/student_page.html')

#---------------------------------------------

# Custom User Views
def custom_user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'erp/custom_user_list.html', {'users': users})

def custom_user_create(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = CustomUserForm()
    return render(request, 'erp/form_template.html', {'form': form})

def custom_user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('custom_user_list')
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'erp/form_template.html', {'form': form})

def custom_user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('custom_user_list')
    return render(request, 'erp/confirm_delete.html', {'object': user})

# Dept Views
def dept_list(request):
    depts = Dept.objects.all()
    return render(request, 'erp/dept_list.html', {'depts': depts})

def dept_create(request):
    if request.method == 'POST':
        form = DeptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dept_list')
    else:
        form = DeptForm()
    return render(request, 'erp/form_template.html', {'form': form})

def dept_update(request, pk):
    dept = get_object_or_404(Dept, pk=pk)
    if request.method == 'POST':
        form = DeptForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            return redirect('dept_list')
    else:
        form = DeptForm(instance=dept)
    return render(request, 'erp/form_template.html', {'form': form})

def dept_delete(request, pk):
    dept = get_object_or_404(Dept, pk=pk)
    if request.method == 'POST':
        dept.delete()
        return redirect('dept_list')
    return render(request, 'erp/confirm_delete.html', {'object': dept})

# Course Views
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'erp/course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'erp/form_template.html', {'form': form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'erp/form_template.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'erp/confirm_delete.html', {'object': course})

# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'erp/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_page')
    else:
        form = StudentForm()
    return render(request, 'erp/form_template.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'erp/form_template.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'erp/confirm_delete.html', {'object': student})

# Teacher Views
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'erp/teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_page')
    else:
        form = TeacherForm()
    return render(request, 'erp/form_template.html', {'form': form})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'erp/form_template.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'erp/confirm_delete.html', {'object': teacher})

# Assign Views
def assign_list(request):
    assigns = Assign.objects.all()
    return render(request, 'erp/assign_list.html', {'assigns': assigns})

def assign_create(request):
    if request.method == 'POST':
        form = AssignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assign_list')
    else:
        form = AssignForm()
    return render(request, 'erp/form_template.html', {'form': form})

def assign_update(request, pk):
    assign = get_object_or_404(Assign, pk=pk)
    if request.method == 'POST':
        form = AssignForm(request.POST, instance=assign)
        if form.is_valid():
            form.save()
            return redirect('assign_list')
    else:
        form = AssignForm(instance=assign)
    return render(request, 'erp/form_template.html', {'form': form})

def assign_delete(request, pk):
    assign = get_object_or_404(Assign, pk=pk)
    if request.method == 'POST':
        assign.delete()
        return redirect('assign_list')
    return render(request, 'erp/confirm_delete.html', {'object': assign})

# Attendance Views
def attendance_list(request):
    attendances = Attendance.objects.all()
    return render(request, 'erp/attendance_list.html', {'attendances': attendances})

def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'erp/form_template.html', {'form': form})

def attendance_update(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
    return render(request, 'erp/form_template.html', {'form': form})

def attendance_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')
    return render(request, 'erp/confirm_delete.html', {'object': attendance})

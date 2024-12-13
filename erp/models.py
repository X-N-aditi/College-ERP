from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from datetime import date, timedelta
from django.dispatch import receiver
from django.utils.timezone import now
#............................................................

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]
Branch = [
    ('CSE', 'Computer Science Engineering'),
    ('ME', 'Mechenical Engineering'),
    ('BT', 'Biotechnical'),
    ('ECE', 'Electronics and Communication Enginnering'),
    ('CE', 'Civil Engineering'),
    ('IT', 'Information Technology'),
    ('EE', 'Electrical Engineering')
]
time_slots = [
    ('9:00 - 9:40', '9:00 - 9:40'),
    ('9:40 - 10:20', '9:40 - 10:20'),
    ('10:20 - 11:00', '10:20 - 11:00'),
    ('11:00 - 11:40', '11:00 - 11:40'),
    ('11:40 - 12:20', '11:40 - 12:20'),
    ('12:20 - 1:20', '12:20 - 1:20'),
    ('1:20 - 2:00', '1:20 - 2:00'),
    ('2:00 - 2:40', '2:00 - 2:40'),
    ('2:40 - 3:20', '2:40 - 3:20'),
    ('3:20 - 4:00', '3:20 - 4:00'),
]

Days_of_week = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
]

#......................................................

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.CharField(max_length=3, choices=[('yes', 'yes'), ('no', 'no')], default='yes')
    is_staff = models.CharField(max_length=3, choices=[('yes', 'yes'), ('no', 'no')], default='no')
    is_student = models.CharField(max_length=3, choices=[('yes', 'yes'), ('no', 'no')], default='yes')
    is_teacher = models.CharField(max_length=3, choices=[('yes', 'yes'), ('no', 'no')], default='no')
    date_joined = models.DateField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Specify a custom related_name
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Specify a custom related_name
        blank=True
    )

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    

    

#..................................................

class Dept(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, default="Engineering")
    
    def __str__(self):
        return self.name
    
#...........................................................

class Course(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=Branch, default='CSE')
    shortname = models.CharField(max_length=50, default='X')

    def __str__(self):
        return self.name
    
#......................................................................

class Class(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='Engineering')
    section = models.CharField(max_length=100)
    sem = models.IntegerField()

    class Meta:
        verbose_name_plural = 'classes'

    def __str__(self):
        d = Dept.objects.get(name=self.name)
        return f"Department :{d.name}, Sem : {self.sem}, Section : {self.section}"
        

#.....................................

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    password = models.CharField(max_length=25, default='abcd1234')
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)
    USN = models.CharField(primary_key=True, max_length=100)
    enrollment_no = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return f"Student: {self.user.email}, Enrollment No: {self.enrollment_no}"




#.........................................................

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    password = models.CharField(max_length=25, default='abcd1234')
    id = models.CharField(primary_key=True, max_length=100)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return f"Teacher: {self.user.email}, Dept: {self.dept.name}"
    
#.........................................................

class Assign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('course', 'class_id', 'teacher'),)

    def __str__(self):
        return '%s : %s : %s' % (self.teacher.user.email, self.course.name, self.class_id.id)
    
#...................................................

class AssignTime(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    period = models.CharField(max_length=50, choices=time_slots, default='9:00 - 9:40')
    day = models.CharField(max_length=15, choices=Days_of_week, default='Monday')

#................................................


class AttendanceClass(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    status = models.CharField(max_length=20, default='Pending', choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return self.status

    
#............................................................

class Attendance(models.Model):
    attendance_class = models.ForeignKey(AttendanceClass, on_delete=models.CASCADE, default=1)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default='2024-12-11')
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.enrollment_no} - {self.attendance_class.date} - {self.status}"

#..................................................................


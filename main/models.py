from django.db import models
from django.forms.models import model_to_dict
import json
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
"""subjects should be referenced to classes, on student view send the subjects
in a table, on teachers view it should also be a table but of students names.
users shoudld inherit from django users model"""


class CustomUserManager(BaseUserManager):
    def create_user(self, identifier, password=None, **extra_params):
        if not identifier:
            raise ValueError('You must provide a valid id')
        
        new_user = self.model(identifier=identifier, **extra_params)
        new_user.set_password(password)
        new_user.save()
        return new_user
    
    def create_superuser(self, identifier, **extra_params):
        extra_params.setdefault('is_staff', True)
        extra_params.setdefault('is_superuser', True)
        
        return self.create_user(identifier, **extra_params)


class CustomUser(AbstractBaseUser):
    ROLE_CHOICES = [
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, default='', null=True)
    identifier = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'other_name': self.other_name,
            'role': self.role,
            'phone_number': self.phone_number,
            'created_on': self.created_on,
            'updated_on': self.updated_on
        }

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['first_name']
        
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'identifier'
    

class Teacher(CustomUser):
    email = models.EmailField(max_length=254)
    level = models.IntegerField(verbose_name='worker_level', default=1)
    salary = models.DecimalField(max_digits=6, decimal_places=2,
                                 default=000.00)

    def __str__(self):
        return self.get_full_name()
    
    EMAIL_FIELD = 'email'


class Student(CustomUser):
    current_class = models.ForeignKey("Grade", on_delete=models.SET_NULL,
                                      null=True)
    subjects = models.ManyToManyField('Subject')

    def to_json(self):
        return json.dumps(model_to_dict(self))

    def __str__(self):
        return self.first_name.__str__() + self.current_class.__str__() +\
    self.subjects.__str__()


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_class = models.ForeignKey("Grade", related_name='grade',
                                      on_delete=models.CASCADE)
    teacher_name = models.ForeignKey("Teacher", on_delete=models.SET_NULL,
                                     null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['subject_name']

    def __str__(self):
        return {
            'subject_name': self.subject_name,
            'subject_class': self.subject_class,
            'teacher_name': self.teacher_name
        }


class Grade(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def to_json(self):
        return {
            'category': self.category,
            'name': self.name
        }

    def __str__(self):
        return self.category + ':' + self.name

    def __unicode__(self):
        return self.name


class ContinousAssessment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    first_ca = models.IntegerField(default=0)
    second_ca = models.IntegerField(default=0)
    third_ca = models.IntegerField(default=0)
    exams = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    def to_json(self):
        return {
            'subject': self.subject.subject_name,
            'student': self.student.name,
            'first_ca': self.first_ca,
            'second_ca': self.second_ca,
            'third_ca': self.third_ca,
            'exams': self.exams,
            'total': self.total
        }

from django.db import models
from django.forms.models import model_to_dict
import json
# from django.contrib.auth.models import AbstractUser
# Create your models here.
"""subjects should be referenced to classes, on student view send the subjects
in a table, on teachers view it should also be a table but of students names.
users shoudld inherit from django users model"""


class User(models.Model):
    ROLE = [
        ('TEACHER', 'teacher'),
        ('STUDENT', 'student'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, default=None, null=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
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

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ['first_name']


class Teacher(User):
    level = models.IntegerField(verbose_name='worker_level', default=1)
    salary = models.DecimalField(max_digits=6, decimal_places=2,
                                 default=000.00)

    def __str__(self):
        return self.first_name + '' + self.last_name


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


class Student(User):
    current_class = models.ForeignKey("Grade", on_delete=models.SET_NULL,
                                      null=True)
    subjects = models.ManyToManyField('Subject')

    def to_json(self):
        return json.dumps(model_to_dict(self))

    def __str__(self):
        return self.first_name.__str__() + self.current_class.__str__() +\
    self.subjects.__str__()


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

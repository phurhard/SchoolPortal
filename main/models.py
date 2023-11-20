from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
"""subjects should be referenced to classes, on student view send the subjects
in a table, on teachers view it should also be a table but of students names.
users shoudld inherit from django users model"""


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, default=None, null=True)
    password = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['first_name']


class Teacher(User):
    phone_number = models.CharField(max_length=20)


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_class = models.ForeignKey("Grade", related_name='grade',
                                      on_delete=models.CASCADE)
    teacher_name = models.ForeignKey("Teacher", on_delete=models.SET_NULL,
                                     null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Student(User):
    current_class = models.ForeignKey("Grade", on_delete=models.SET_NULL,
                                      null=True)
    subjects = models.ManyToManyField('Subject')


class Grade(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

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

from django.db import models
from django.forms.models import model_to_dict
import json
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
"""subjects should be referenced to classes, on student view send the subjects
in a table, on teachers view it should also be a table but of students names.
users shoudld inherit from django users model"""


class CustomUserManager(BaseUserManager):
    def create_user(self, identifier, password=None, **extra_params):
        if not identifier:
            raise ValueError('You must provide a valid id')
        
        new_user = self.model(reg_num=identifier, **extra_params)
        new_user.set_password(password)
        new_user.save()
        return new_user
    
    def create_superuser(self, reg_num, **extra_params):
        extra_params.setdefault('is_staff', True)
        extra_params.setdefault('is_superuser', True)
        
        return self.create_user(reg_num, **extra_params)

class CustomUser(AbstractUser):
    # ROLE_CHOICES = [
    #     ('Teacher', 'Teacher'),
    #     ('Student', 'Student'),
    # ]
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, default='', null=True)
    reg_num = models.CharField(max_length=255, unique=True)
    username = None
    phone_number = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'other_name': self.other_name,
            'reg_num': self.reg_num,
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
        # abstract = True
        
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'reg_num'
    REQUIRED_FIELDS = []

# @receiver(post_save, sender=CustomUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.role == 'Teacher':
#             Teacher.objects.create(email=instance.email, admin=instance)
#         elif instance.role == 'Student':
#             Student.objects.create(current_class=None, admin=instance)

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.role == 'Teacher':
#         instance.teacher.save()
#     elif instance.role == 'Student':
#         instance.student.save()

class Teacher(CustomUser):
    # email = models.EmailField(max_length=254)
    level = models.IntegerField(verbose_name='worker_level', default=1)
    salary = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.get_full_name()
    
    # EMAIL_FIELD = 'email'
    class Meta:
        db_table = 'Teacher'

class Student(CustomUser):
    current_class: object = models.ForeignKey("Grade", on_delete=models.SET_NULL, null=True)
    subjects: object = models.ManyToManyField('Subject')

    def to_json(self):
        return json.dumps(model_to_dict(self))

    def __str__(self):
        return self.get_full_name() + str(self.current_class) + str(self.subjects)

    class Meta:
        db_table = 'Student'

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_class = models.ForeignKey("Grade", related_name='subjects', on_delete=models.CASCADE)
    teacher_name = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['subject_name']

    def __str__(self):
        return f'{self.subject_name} ({self.subject_class}) - {self.teacher_name}'

class Grade(models.Model):
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def to_json(self):
        return {
            'category': self.category,
            'name': self.name
        }

    def __str__(self):
        return f'{self.category}: {self.name}'

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
            'student': self.student.get_full_name,
            'first_ca': self.first_ca,
            'second_ca': self.second_ca,
            'third_ca': self.third_ca,
            'exams': self.exams,
            'total': self.total
        }

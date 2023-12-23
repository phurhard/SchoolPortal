from django.db import models
from django.forms.models import model_to_dict
import json
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save, pre_save
from django.http import Http404
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


class Teacher(CustomUser):
    level = models.IntegerField(verbose_name='worker_level', default=1)
    salary = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.get_full_name()
    
    class Meta:
        db_table = 'Teacher'

class Student(CustomUser):
    current_class = models.ForeignKey("Grade", on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField('Subject')

    def to_json(self):
        return json.dumps(model_to_dict(self))

    def __str__(self):
        return f'{self.get_full_name()} {str(self.current_class)}'

    class Meta:
        db_table = 'Student'

# Signal function to handle subject assignment to students
@receiver(post_save, sender=Student)
def assign_subjects_to_student(sender, instance, created, **kwargs):
    if created:
        # If the student is newly created, assign subjects for their class
        student_class = instance.current_class
        subjects_for_class = Subject.objects.filter(subject_class=student_class)
        instance.subjects.add(*subjects_for_class)

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_class = models.ForeignKey("Grade", related_name='subjects', on_delete=models.CASCADE, default=None)
    teacher_name = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['subject_name']

    def save(self, *args, **kwargs):
        """Overriding the main functionality so that before it is saved,
        it'll add a CA to itself and also check if it does not exists before to prevent repetition"""
        if Subject.objects.filter(subject_name=self.subject_name, subject_class=self.subject_class).exists():
            return
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.subject_name} ({self.subject_class}) - {self.teacher_name}'

@receiver(pre_save, sender=Student)
def check_subjects(sender, instance, **kwargs):
    """Checks if the subject selected are the subjects allocated to that class"""
    for subject in instance.subjects.all():
        if subject.subject_class != instance.current_class:
            break

@receiver(post_save, sender=Student)
def assign_continous_assessment(sender, instance, created, **kwargs):
    """Automatically assings continous assessment to a specific subject to a student."""
    # need to reconfigure this to ensure once a student is not in a grade all ca for that grade shoul be removed from the student info
    # or better still it should not be removed, since its a log
    if created or not created:
        for subject in instance.subjects.all():
            ContinousAssessment.objects.create(subject=subject, student=instance)
            # CA.subject = instance
            # CA.save()
            print(f'successful {subject} added')
            # the print statement is a checker to confirm it is working
            # print(f'the CA: \n{}')


class Grade(models.Model):
    CLASS_SEGMENT = [
        ('Pre_JSS', 'Pre_JSS'),
        ('Nursery', 'Nursery'),
        ('Primary', 'Primary'),
        ('Junior Secondary', 'Junior Secondary'),
        ('Senior Secondary', 'Senior Secondary'),
        ]
    
    # MEDIA_CHOICES = [
    #     (
    #         "Audio",
    #         (
    #             ("vinyl", "Vinyl"),
    #             ("cd", "CD"),
    #         ),
    #     ),
    #     (
    #         "Video",
    #         (
    #             ("vhs", "VHS Tape"),
    #             ("dvd", "DVD"),
    #         ),
    #     ),
    #     ("unknown", "Unknown"),
    #     ]
    category = models.CharField(max_length=200, choices=CLASS_SEGMENT, default="Nursery", null=True)
    name = models.IntegerField()
    # change the name to int, and make it unique, so only one class can be created

    def to_json(self):
        return {
            'category': self.category,
            'name': self.name
        }

    def save(self, *args, **kwargs):
        if Grade.objects.filter(category=self.category, name=self.name).exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        # main_category = next((dict(choices).values() for category, choices in self.MEDIA_CHOICES if self.category in dict(choices)), None)
        return f'{self.category}: {self.name}'

    def __unicode__(self):
        return self.name


class ContinousAssessment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, default=None)
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

    def save(self, *args, **kwargs):
        if ContinousAssessment.objects.filter(subject=self.subject, student=self.student).exists():
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return f'ContinousAssessment of {self.subject} for {self.student.get_full_name()}'

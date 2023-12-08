from django.contrib import admin
from .models import CustomUser, Subject, Grade, ContinousAssessment
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(ContinousAssessment)
admin.site.register(Grade)
admin.site.register(Subject)

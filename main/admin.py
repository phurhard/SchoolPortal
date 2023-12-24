from django.contrib import admin
from .models import CustomUser, Subject, Grade, ContinousAssessment
# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    list_filter = ["is_staff", "first_name", "last_name", "email", "other_name"]
class ContinousAssessmentAdmin(admin.ModelAdmin):
    list_filter = ['total', 'student', 'subject']

class GradeAdmin(admin.ModelAdmin):
    list_filter = ['category', 'name']
    
class SubjectAdmin(admin.ModelAdmin):
    list_filter = ['subject_name', 'teacher_name', 'subject_class']

# class StudentSubjectAdmin(admin.ModelAdmin):
#     list_filter = ['subject', 'student']

admin.site.register(CustomUser, CustomAdmin)
admin.site.register(ContinousAssessment, ContinousAssessmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Subject, SubjectAdmin)
# admin.site.register(StudentSubjects, StudentSubjectAdmin)

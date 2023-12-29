from django.contrib import admin
from .models import CustomUser, Subject, Grade, ContinousAssessment, Section, Class
# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    list_filter = ["is_staff", "first_name", "last_name", "email", "other_name"]


class ContinousAssessmentAdmin(admin.ModelAdmin):
    list_filter = ['total', 'student', 'subject']


class GradeAdmin(admin.ModelAdmin):
    list_filter = ['category', 'name']


class SubjectAdmin(admin.ModelAdmin):
    list_filter = ['subject_name', 'teacher_name', 'subject_class']


class SectionAdmin(admin.ModelAdmin):
    list_filter = ['name', 'parent']


class ClassAdmin(admin.ModelAdmin):
    list_filter = ['name', 'section']


admin.site.register(CustomUser, CustomAdmin)
admin.site.register(ContinousAssessment, ContinousAssessmentAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Class, ClassAdmin)

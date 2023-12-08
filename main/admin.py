from django.contrib import admin
from .models import CustomUser, Subject, Grade, ContinousAssessment
# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    list_filter = ["is_staff", "first_name", "last_name", "email", "other_name"]
   
admin.site.register(CustomUser, CustomAdmin)
admin.site.register(ContinousAssessment)
admin.site.register(Grade)
admin.site.register(Subject)

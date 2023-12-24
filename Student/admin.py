from django.contrib import admin
from main.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name", "Reg_num"]
admin.site.register(Student, StudentAdmin)

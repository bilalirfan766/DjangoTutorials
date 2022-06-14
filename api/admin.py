from django.contrib import admin
from .models import Student

# Register your models here.
class StudentModel(admin.ModelAdmin):
    list_display = ("id", "name", "roll", "city")


admin.site.register(Student)
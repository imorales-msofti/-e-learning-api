from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Course._meta.fields if field.name != "id"]

admin.site.register(Course, CourseAdmin)

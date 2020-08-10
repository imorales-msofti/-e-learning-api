from django.contrib import admin
from .models import Lesson

class LessonAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Lesson._meta.fields if field.name != "id"]

admin.site.register(Lesson, LessonAdmin)


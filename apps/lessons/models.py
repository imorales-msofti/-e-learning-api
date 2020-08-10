from django.db import models
from apps.courses.models import Course

# Create your models here.
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    previous_lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

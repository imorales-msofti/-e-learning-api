from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)
    previous_course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

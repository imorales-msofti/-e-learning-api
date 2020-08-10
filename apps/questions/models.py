from django.db import models

from apps.lessons.models import Lesson

# Create your models here.
class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    question_type = models.CharField(max_length=50, choices=[
        ('boolean', 'Boolean'),
        ('only_one', 'Only one answer is correct'),
        ('more_than_one', 'More than one answer is correct'),
        ('more_than_one_all_must_correctly', 'More than one answer is correct and all of them must be answered correctly'),
    ])
    choises = models.CharField(max_length=50, choices=[
        ('boolean', 'Boolean'),
        ('only_one', 'Only one answer is correct'),
        ('more_than_one', 'More than one answer is correct'),
        ('more_than_one_all_must_correctly', 'More than one answer is correct and all of them must be answered correctly'),
    ])
    correct_answer = models.CharField(max_length=200)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.name}'



class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField()
    score = models.IntegerField()

    def __str__(self):
        return f'{question.name}: {self.answer}'




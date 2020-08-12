from django.db import models
from django.contrib.postgres.fields import ArrayField
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
    posible_answers =  ArrayField(
            models.CharField(max_length=50, blank=False),
            size=3,
        )
    correct_answer = models.CharField(max_length=200)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.name}'



class ChoiseByQuestion(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    correct = models.BooleanField()

    def __str__(self):
        return f'{question.name}: {self.name}'


class Answer(models.Model):
    choise_by_question = models.ForeignKey('ChoiseByQuestion', on_delete=models.CASCADE)
    correct = models.BooleanField()
    score = models.IntegerField()

    def __str__(self):
        return f'{question.name}: {self.answer}'

from .models import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['lesson', 'name', 'question_type', 'posible_answers']

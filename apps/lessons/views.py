from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, authentication_classes,
                                       parser_classes, permission_classes)
from rest_framework.response import Response
from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer

from .models import Lesson
from .serializers import LessonSerializer

# Create your views here.

class LessonViewSet(viewsets.ModelViewSet):
  
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = []

###Obtiene las lecciones con base al Curso
@api_view(['GET'])
def getQuestions(request, lesson_id):
    questions = Question.objects.filter(lesson_id = lesson_id)
    questions_serializer = QuestionSerializer(questions, many=True)
    return Response({'data': questions_serializer.data}, status=status.HTTP_200_OK)

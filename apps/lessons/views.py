from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, authentication_classes,
                                       parser_classes, permission_classes)
from rest_framework.response import Response
from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer

from .models import Lesson
from .serializers import LessonSerializer
from .services import getCalificacionRespuestas

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

@api_view(['POST'])
def takeLesson(request, lesson_id):
    request_data = request.data.copy()

    try:
        score_respuestas = getCalificacionRespuestas(request_data["respuestas"], lesson_id)
    except Exception as excep:
        return Response({'error': str(excep)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'data': {"score_respuestas": 0}}, status=status.HTTP_200_OK)
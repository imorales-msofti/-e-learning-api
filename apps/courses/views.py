from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import (api_view, authentication_classes,
                                       parser_classes, permission_classes)
from rest_framework.response import Response

from .models import Course
from apps.lessons.models import Lesson
from apps.lessons.serializers import LessonSerializer
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []

###Obtiene las lecciones con base al Curso
@api_view(['GET'])
def getLessons(request, course_id):
    lessons = Lesson.objects.filter(course_id = course_id)
    lessons_serializer = LessonSerializer(lessons, many=True)
    return Response({'data': lessons_serializer.data}, status=status.HTTP_200_OK)

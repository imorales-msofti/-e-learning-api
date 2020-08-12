from django.shortcuts import render
from .serializers import LessonSerializer
from .models import Lesson
from rest_framework import viewsets

# Create your views here.

class LessonViewSet(viewsets.ModelViewSet):
  
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = []
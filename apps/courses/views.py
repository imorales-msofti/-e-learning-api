from django.shortcuts import render
from .serializers import CourseSerializer
from .models import Course
from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []
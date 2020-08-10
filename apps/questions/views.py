from django.shortcuts import render
from .serializers import QuestionSerializer
from .models import Question
from rest_framework import viewsets

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = []
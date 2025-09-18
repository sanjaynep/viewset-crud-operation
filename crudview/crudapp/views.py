from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import DetailSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=DetailSerializer
    

# Create your views here.

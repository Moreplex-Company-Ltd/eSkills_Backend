from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from lessons.serializers import CategoriesSerializer, CourseSerializer, ModulesSerializer, LessonsSerializer, Lesson_ResourcesSerializer, User_InterestSerializer
from lessons.models import Categories, Course, Modules, Lessons, Lesson_Resources, User_Interest
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ModulesViewSet(viewsets.ModelViewSet):
    queryset = Modules.objects.all()
    serializer_class = ModulesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class Lesson_ResourcesViewSet(viewsets.ModelViewSet):
    queryset = Lesson_Resources.objects.all()
    serializer_class = Lesson_ResourcesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class User_InterestViewSet(viewsets.ModelViewSet):
    queryset = User_Interest.objects.all()
    serializer_class = User_InterestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
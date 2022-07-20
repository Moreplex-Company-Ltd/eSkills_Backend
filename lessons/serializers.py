from rest_framework import serializers
from django.template.defaultfilters import slugify
from lessons.models import Categories, Course, Modules, Lessons, Lesson_Resources, User_Interest

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = '__all__'

class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'

class Lesson_ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson_Resources
        fields = '__all__'

class User_InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Interest
        fields = '__all__'

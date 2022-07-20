from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField()
    category_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

class Course (models.Model):
    category_id = models.ForeignKey(Categories)
    course_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField()
    course_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

class Modules (models.Model):
    module_name = models.CharField()
    course_id = models.ForeignKey(Course)
    category_id = models.ForeignKey()
    
class Lessons (models.Model):
    lesson_name = models.CharField()
    module_id = models.ForeignKey(Modules)
    course_id = models.ForeignKey(Course)
    category_id = models.ForeignKey(Categories)
    lesson_video = models.FileField()
    
class Lesson_Resources (models.Model):
    resource_filename = models.CharField()
    lesson_resource = models.FileField()
    course_id = models.ForeignKey(Course)

class User_Interest (models.Model):
    user_id = models.ForeignKey(User)
    category_id = models.ForeignKey(Categories)
    course_id = models.ForeignKey(Course)

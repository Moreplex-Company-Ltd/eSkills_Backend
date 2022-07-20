from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser

class Categories(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField()
    category_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField()
    course_description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()

class Modules(models.Model):
    module_name = models.CharField(max_length=255)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    
class Lessons(models.Model):
    lesson_name = models.CharField(max_length=255)
    module_id = models.ForeignKey(Modules, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    lesson_video = models.FileField()
    
class Lesson_Resources(models.Model):
    resource_filename = models.CharField(max_length=255)
    lesson_resource = models.FileField()
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

class User_Interest(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

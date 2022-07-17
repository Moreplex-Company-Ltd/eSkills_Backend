from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # We don't need to define the email attribute because is inherited from AbstractUser
    phone_number = models.CharField(max_length=30)
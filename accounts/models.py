from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    name = models.CharField(null=True, blank=True, max_length=100)
    password = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    user_score = models.IntegerField()
    user_role = models.CharField(max_length=100)

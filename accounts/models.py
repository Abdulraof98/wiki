from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100)
    name = models.CharField(null=True, blank=True, max_length=100)
    age = models.PositiveSmallIntegerField(null=True, default=18)
    user_score = models.IntegerField(null=True)
    user_role = models.CharField(max_length=100)

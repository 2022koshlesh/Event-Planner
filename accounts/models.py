from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("planner", "Event Planner"),
        ("guest", "Guest"),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="planner")
    phone_number = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.username


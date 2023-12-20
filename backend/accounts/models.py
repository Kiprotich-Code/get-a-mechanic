from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('mechanic', 'Mechanic'),
        ('car_owner', 'Car_Owner'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='Customer')